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

int mx[200];
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        int size, n;
        scanf("%d%d", &size, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &mx[i]);
        }
        sort(mx, mx + n);

        if (size == 1) {
            printf("%d\n", n);
            continue;
        }
        int nums[200] = {0};
        int res = 0;
        for (int i = 0; i < n; i++) {
            while (1) {
                if (size > mx[i]) {
                    size += mx[i];
                    break;
                }
                size = size + size -1;
                res++;
            }
            nums[i] = res;
        }
        int minv = res;
        for (int i = n - 1; i >= 0; i--) {
            if (minv <= 0) {
                break;
            }
            if (i > 0) {
                minv = min(minv, nums[i - 1] + (n - i));
            } else {
                minv = min(minv, n);
            }
        }
        printf("%d\n", minv);
    }
	return 0;
}
