/* This is template part fro Google CodeJam contest
 * created by Shapovalov Nikita, 2014
 */

#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

namespace CodeJamUtility {

    class TestCaseUtil
    {
        std::clock_t start_test_time;

        int test_id_;

        std::stringstream ss;

    public:
        TestCaseUtil(int test_id) : start_test_time(std::clock()), test_id_(test_id), ss()
        {
            std::cerr << "Processing test #" << std::setw(4) << test_id << ": ";
        }

        TestCaseUtil(const TestCaseUtil &) = delete;

        TestCaseUtil &operator=(const TestCaseUtil &) = delete;

        ~TestCaseUtil()
        {
            std::cerr << "Ok. Time elapsed: " << std::setw(5) << 
                (std::clock() - start_test_time) / (1. * CLOCKS_PER_SEC) << " secs" << std::endl;
            std::cout << "Case #" << test_id_ << ": " << ss.str() << "\n";
        }

        template< class T >
        friend TestCaseUtil &operator<<(TestCaseUtil &, const T &obj);

    };

    template< class T >
    TestCaseUtil &
    operator<<(TestCaseUtil &t, const T &obj)
    {
        t.ss << obj;
        return t;
    }
}

#define EXECUTE_FUNCTION(NAME) \
    process(CodeJamUtility::TestCaseUtil & NAME)

#define CODEJAM_RUN_NEW_TEST(ID, NAME) \
    {\
        CodeJamUtility::TestCaseUtil NAME(ID);\
        process(NAME);\
    }

#define CODEJAM_RUN_ALL_TESTS(NAME)\
int main() \
{\
    int testNumber##NAME;\
    std::cin >> testNumber##NAME;\
    for (int counter##NAME = 1; counter##NAME <= testNumber##NAME; ++counter##NAME) {\
        CODEJAM_RUN_NEW_TEST(counter##NAME, NAME);\
    }\
    return 0;\
}

/* End of template part */


#include <vector>
#include <algorithm>
#include <climits>
#include <utility>

using namespace std;

void
updMin(int &dst, int src)
{
    if (dst > src) {
        dst = src;
    }
}

void
EXECUTE_FUNCTION(out)
{
    int n;
    cin >> n;
    vector< pair< int, int > > ids;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        ids.push_back(make_pair(x, i));
    }
    sort(ids.begin(), ids.end());
    vector< int > vp(n, 0);
    for (int i = 0; i < n; ++i) {
        vp[ids[i].second] = i;
    }
    ids.clear();
    vector< int > lc(n, 0), rc(n, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (vp[j] > vp[i]) {
                ++lc[vp[i]];
            }
        }
        for (int j = i + 1; j < n; ++j) {
            if (vp[j] > vp[i]) {
                ++rc[vp[i]];
            }
        }
    }
    vector< vector< int > > dp;
    dp.resize(n + 1);
    for (int i = 0; i <= n; ++i) {
       dp[i].resize(n + 1, INT_MAX >> 3);
    }
    dp[0][0] = 0;
    for (int sum = 0; sum < n; ++sum) {
        for (int l = 0; l <= sum; ++l) {
            int r = sum - l;
            int next_num = sum;
            updMin(dp[l + 1][r], dp[l][r] + lc[next_num]);
            updMin(dp[l][r + 1], dp[l][r] + rc[next_num]);
        }
    }
    int res = INT_MAX;
    for (int i = 0; i <= n; ++i) {
        updMin(res, dp[i][n - i]);
    }
    out << res;
}

CODEJAM_RUN_ALL_TESTS(Round2_B_2014)
