#include <stack>
#include <cstdio>
#include <list>
#include <cassert>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <map>
#include <cmath>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/hash_policy.hpp>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define SZ(x) (int)x.size()
#define Lowbit(x) ((x) & (-x))
#define MP(a, b) make_pair(a, b)
#define MS(arr, num) memset(arr, num, sizeof(arr))
#define PB push_back
#define X first
#define Y second
#define ROP freopen("input.txt", "r", stdin);
#define MID(a, b) (a + ((b - a) >> 1))
#define LC rt << 1, l, mid
#define RC rt << 1|1, mid + 1, r
#define LRT rt << 1
#define RRT rt << 1|1
const double PI = acos(-1.0);
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int MAXN = 1000+10;
const int MOD = 2012;
const int dir[][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
int cases = 0;
typedef pair<int, int> pii;

int arr[MAXN];
int main()
{
    ROP;
    freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	while (T--)
	{
		int n, maxVal = -1;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &arr[i]);
			maxVal = max(maxVal, arr[i]);
		}
		int ans = INF;
		for (int j = 1; j <= maxVal; j++)
		{
			int curAns = 0;
			for (int i = 0; i < n; i++)
            {
                int cnt = 0, tmp = arr[i];
                while (tmp > j)
                {
                    tmp -= j;
                    cnt++;
                }
                curAns += cnt;
            }
			ans = min(ans, curAns + j);
		}
		printf("Case #%d: %d\n", ++cases, ans);
	}
	return 0;
}

