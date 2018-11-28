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
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/hash_policy.hpp>
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

string str;
bool Check(int n)
{
	int curLeave = n;
	for (int i = 0; i < SZ(str); i++)
	{
		if (i == 0) { curLeave += str[i]-'0'; continue; }
		if (curLeave < i) return false;
		curLeave += str[i]-'0';
	}
	return true;
}

int main()
{
    ROP;
    freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	while (T--)
	{
		int n;
		cin >> n >> str;
		int l = 0, r = n+1;
		while (l < r)
		{
			int mid = MID(l, r);
			if (Check(mid)) r = mid;
			else l = mid+1;
		}
		printf("Case #%d: %d\n", ++cases, r);
	}
	return 0;
}
