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

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define maxn 100500
#define maxalph 26

const int MD = 1000000007;

int go[maxn][maxalph];

inline void
add(int &dst, int src)
{
    dst += src;
    if (dst >= MD) {
        dst -= MD;
    }
}

int
get_number(int mask, int sz, const vector< string > &vs)
{
    int cnt = 1;
    fill(go[cnt], go[cnt] + maxalph, 0);
    for (int i = 0; i < sz; ++i) {
        if (mask & (1 << i)) {
            int cur = 1;
            for (auto x : vs[i]) {
                if (!go[cur][x - 'A']) {
                    go[cur][x - 'A'] = ++cnt;
                    fill(go[cnt], go[cnt] + maxalph, 0);
                }
                cur = go[cur][x - 'A'];
            }
        }
    }
    return cnt;
}

void
EXECUTE_FUNCTION(out)
{
    int m, n;
    cin >> m >> n;
    vector< string > s(m);
    vector< vector< int > > ans(m + 1), cnt(m + 1);
    for (int i = 0; i < m; ++i) {
        cin >> s[i];
    }
    vector< int > nums;
    for (int i = 0; i < (1 << m); ++i) {
        nums.push_back(get_number(i, m, s));
    }
    /*for (auto x : nums) {
        cerr << x << " ";
    }
    cerr << endl;*/
    for (int i = 0; i <= m; ++i) {
        ans[i].assign((1 << m), 0);
        cnt[i].assign((1 << m), 0);
    }
    cnt[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j < (1 << m); ++j) {
            for (int k = 0; k < j; ++k) {
                if ((k & j) == k && k != j) {
                    int l = j ^ k;
                    /*if (cnt[i - 1][k] == 0) {
                        continue;
                    }*/
                    if (ans[i][j] < ans[i - 1][k] + nums[l]) {
                        //cerr << "upd " << i << " " << j << " " << k << endl;
                        ans[i][j] = ans[i - 1][k] + nums[l];
                        cnt[i][j] = 0;
                    }
                    if (ans[i][j] == ans[i - 1][k] + nums[l]) {
                        add(cnt[i][j], cnt[i - 1][k]);
                    }
                }
            }
        }
    }
    out << ans[n][(1 << m) - 1] << " " << cnt[n][(1 << m) - 1];
}

CODEJAM_RUN_ALL_TESTS(Round2_D_2014)
