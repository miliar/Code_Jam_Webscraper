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

void main2()
{
    int x, y;
    cin >> x >> y;
    if (x > 0) {
        for (int i = 0; i < x; i++) {
            printf("WE");
        }
    } else {
        int xx = -x;
        for (int i = 0; i < xx; i++) {
            printf("EW");
        }
    }
    if (y > 0) {
        for (int i = 0; i < y; i++) {
            printf("SN");
        }
    } else {
        int yy = -y;
        for (int i = 0; i < yy; i++) {
            printf("NS");
        }
    }
    printf("\n");
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        main2();
    }
	return 0;
}
