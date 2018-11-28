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
        int precision;

        std::stringstream ss;

    public:
        TestCaseUtil(int test_id, int precision_ = 13) : 
            start_test_time(std::clock()),
            test_id_(test_id),
            precision(precision_),
            ss()
        {
            ss << std::fixed << std::setprecision(precision);
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

#include <algorithm>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;

ll
check(int l, int r, int n, vector< ll > &sum)
{
    ll cur = max(sum[r], sum[l] - sum[r]);
    if (r != n) {
        cur = min(cur, max(sum[r + 1], sum[l] - sum[r + 1]));
    }
    cur = max(cur, sum[0] - sum[l]);
    return cur;
}

void
EXECUTE_FUNCTION(out)
{
    int n, p, q, md, s;
    cin >> n >> p >> q >> md >> s;
    vector< int > all(n);
    vector< ll > sum(n + 1);
    for (int i = 0; i < n; ++i) {
        all[i] = ((1ll * i * p + q) % md + s);
    }
    sum[n] = 0LL;
    for (int i = n - 1; i >= 0; --i) {
        sum[i] = sum[i + 1] + all[i];
    }
    ll all_s = sum[0], min_part = all_s;
    int r = 0;
    for (int l = 0; l < n; ++l) {
        while (r < n && sum[l] - sum[r + 1] < sum[r + 1]) ++r;
        min_part = min(min_part, check(l, r, n, sum));
    }
    out << ((all_s - min_part) * 1. / all_s);
}

CODEJAM_RUN_ALL_TESTS(Round_3A_2014)
