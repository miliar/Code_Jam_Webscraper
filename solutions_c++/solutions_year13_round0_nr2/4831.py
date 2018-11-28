#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

int mx[100][100];
int main()
{
    int T, casenum = 1; 
    scanf("%d", &T);
    while (T--) {
        int x, y;
        scanf("%d %d", &x, &y);
        bool good = true;
        for (int i = 0; i < (int)x; i++) {
            for (int j = 0; j < (int)y; j++) {
                scanf("%d", &mx[i][j]);
            }
        }
        for (int i = 0; i < (int)x; i++) {
            for (int j = 0; j < (int)y; j++) {
                bool col = true, row = true;
                int val = mx[i][j];
                for (int ii = 0; ii < x; ii++) {
                    if (mx[ii][j] > val) {
                        col = false;
                    }
                }
                for (int jj = 0; jj < y; jj++) {
                    if (mx[i][jj] > val) {
                        row = false;
                    }
                }
                if (!col && !row) {
                    good = false;
                }
            }
        }

        printf("Case #%d: ", casenum++);
        if (good) {
            puts("YES");
        } else  {
            puts("NO");
        }
    }
	return 0;
}
