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
#include <map>
#include <set>
#include <utility>

const int DX[] = {0, -1, 0, 1};
const int DY[] = {-1, 0, 1, 0};

using namespace std;

typedef pair< int, int > pii;

void
check_add(int x, int bord, vector< int > &add)
{
    if (x >= 0 && x < bord) {
        add.push_back(x);
    }
}

bool
ok(int x, int b)
{
    return (x >= 0 && x < b);
}

bool
dfs(int x, int y, int od, int w, int h, vector< vector< int > > &used)
{
    used[x][y] = 1;
    if (y == h - 1) {
        return true;
    }
    od = (od + 3) % 4;
    for (int dir = 0; dir < 4; ++dir) {
        int cx = x + DX[od];
        int cy = y + DY[od];
        if (ok(cx, w) && ok(cy, h) && !used[cx][cy]) {
            bool res = dfs(cx, cy, od, w, h, used);
            if (res) {
                return true;
            }
        }
        od = (od + 1) % 4;
    }
    return false;
}

void
EXECUTE_FUNCTION(out)
{
    int h, w, b;
    cin >> w >> h >> b;
    vector< pair< pii, pii > > build(b);
    vector< int > ycoord;
    check_add(0, h, ycoord);
    check_add(h - 1, h, ycoord);
    for (int i = 0; i < b; ++i) {
        cin >> build[i].first.first >> build[i].first.second 
            >> build[i].second.first >> build[i].second.second;
        int y0 = build[i].first.second, y1 = build[i].second.second;
        for (int diff = -1; diff <= 1; ++diff) {
            check_add(y0 + diff, h, ycoord);
            check_add(y1 + diff, h, ycoord);
        }
    }
    sort(ycoord.begin(), ycoord.end());
    ycoord.resize(unique(ycoord.begin(), ycoord.end()) - ycoord.begin());
    vector< vector< int > > used;
    used.resize(w);
    //h = int(ycoord.size());
    for (int i = 0; i < w; ++i) {
        used[i].assign(h, 0);
    }
    for (int i = 0; i < b; ++i) {
        int x0 = build[i].first.first;
        int x1 = build[i].second.first;
        int &y0 = build[i].first.second;
        int &y1 = build[i].second.second;
        //y0 = lower_bound(ycoord.begin(), ycoord.end(), y0) - ycoord.begin();
        //y1 = lower_bound(ycoord.begin(), ycoord.end(), y1) - ycoord.begin();
        for (int x = x0; x <= x1; ++x) {
            for (int y = y0; y <= y1; ++y) {
                used[x][y] = true;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < w; ++i) {
        if (!used[i][0]) {
            bool ok = dfs(i, 0, 2, w, h, used);
            if (ok) {
                ++res;
            }
        }
    }
    out << res;
}

CODEJAM_RUN_ALL_TESTS(Round2_C_2014)
