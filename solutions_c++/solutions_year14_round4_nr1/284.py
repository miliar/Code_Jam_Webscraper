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
#include <set>

using namespace std;

void
EXECUTE_FUNCTION(out)
{
    int n, x;
    cin >> n >> x;
    vector< int > sp(n);
    for (int i = 0; i < n; ++i) {
        cin >> sp[i];
    }
    sort(sp.rbegin(), sp.rend());
    int res = 0;
    multiset< int > caps;
    for (int i = 0; i < n; ++i) {
        auto it = caps.end();
        if (!caps.empty()) {
            --it;
        }
        if (it == caps.end() || *it < sp[i]) {
            ++res;
            caps.insert(x - sp[i]);
        } else {
            caps.erase(it);
        }
    }
    out << res;
}

CODEJAM_RUN_ALL_TESTS(Round2_A_2014)

