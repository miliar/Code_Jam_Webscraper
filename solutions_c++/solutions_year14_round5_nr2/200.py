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
#include <tuple>
#include <map>
#include <set>
#include <cstring>

using namespace std;

#define maxn 1005

typedef tuple< int, int, int, int > tp;

map< tp, int > st;

int n, p, q;
int hp[maxn];
int gold[maxn];

int
solve(int pl, int pos, int cur_h, int cnt)
{
    auto it = st.find(make_tuple(pl, pos, cur_h, cnt));
    if (it == st.end()) {
        // time to play
        int res = 0;
        if (cur_h <= 0) {
            // killed by Diana
            for (int used_cnt = 0; pos != n && used_cnt <= cnt && used_cnt * p - p <= hp[pos + 1]; ++used_cnt) {
                res = max(res, solve(pl, pos + 1, hp[pos + 1] - used_cnt * p, cnt - used_cnt));
            }
            res += gold[pos];
        } else {
            if (pl == 2) { // tower
                if (q >= cur_h) {
                    for (int used_cnt = 0; pos != n && used_cnt <= cnt && used_cnt * p - p <= hp[pos + 1]; ++used_cnt) {
                        res = max(res, solve(1, pos + 1, hp[pos + 1] - used_cnt * p, cnt - used_cnt));
                    }
                } else {
                    res = solve(1, pos, cur_h - q, cnt);
                }
            } else { // Diana
                // skip turn (simply beat anyone - maybe none - after this monster)
                res = solve(2, pos, cur_h, cnt + 1);
                // beat monster
                if (p >= cur_h) {
                    // if there is any monster
                    int add = 0;
                    if (pos != n) {
                        for (int used_cnt = 0; used_cnt <= cnt && used_cnt * p - p <= hp[pos + 1]; ++used_cnt) {
                            add = max(add, solve(2, pos + 1, hp[pos + 1] - used_cnt * p, cnt - used_cnt));
                        }
                    }
                    // get gold for him
                    res = max(res, add + gold[pos]);
                } else {
                    res = max(res, solve(2, pos, cur_h - p, cnt));
                }
            }
        }
        it = st.insert(make_pair(make_tuple(pl, pos, cur_h, cnt), res)).first;
    }
    //cerr << "here " << pl << " " << pos << " " << cur_h << " " << cnt << "-> " << it->second << endl;
    return it->second;
}

void
EXECUTE_FUNCTION(out)
{
    st.clear();
    cin >> p >> q >> n;
    memset(hp, 0, sizeof(hp));
    memset(gold, 0, sizeof(gold));
    for (int i = 1; i <= n; ++i) {
        cin >> hp[i] >> gold[i];
    }
    int res = solve(1, 1, hp[1], 0);
    out << res;
}

CODEJAM_RUN_ALL_TESTS(Round_3B_2014)
