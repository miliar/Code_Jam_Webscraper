#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

typedef long double ld;
const ld EPS = 1e-9;

clock_t start_test_time = 0;

class TestCaseUtil
{
    clock_t start_test_time;
public:
    TestCaseUtil(int test_id) : start_test_time(clock())
    {
        cerr << "Processing test #" << setw(3) << test_id << ": ";
    }
    TestCaseUtil(const TestCaseUtil &) = delete;
    TestCaseUtil &operator=(const TestCaseUtil &) = delete;
    ~TestCaseUtil()
    {
        cerr << "Ok. Time elapsed: " << setw(5) << 
            (clock() - start_test_time) / CLOCKS_PER_SEC << " secs" << endl;
    }
};

void
process(int test_id)
{
    TestCaseUtil cur_test(test_id);
    ld c(0), f(0), x(0);
    cin >> c >> f >> x;
    cout << "Case #" << test_id << ": ";
    int min_id = 0;
    if (2 * c - x * f <- EPS) {
        min_id = int(x / c - 2. / f);
    }
    ld cur_denom = 2.;
    ld res(0);
    for (int i = 0; i < min_id; ++i) {
        res += c / cur_denom;
        cur_denom += f;
    }
    res += x / cur_denom;
    cout << setprecision(15) << fixed << res << endl;
}

int
main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        process(i);
    }
    return 0;
}
