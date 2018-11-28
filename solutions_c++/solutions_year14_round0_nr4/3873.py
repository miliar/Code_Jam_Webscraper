#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <sstream>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define F(i,a) FOR(i,0,a)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define X first
#define Y second
#define S size()
#define MS(a, v) memset(a, v, sizeof a)
#define NL printf("\n")
#define SP system("pause")
#define INF 1e9
#define PI acos(-1)
#define EPS 1e-9
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> vi;

int t, n;
double vn[1010], vk[1010];

int main()
{
	// ios_base::sync_with_stdio(0);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &t);
	F(tc, t) {
		scanf("%d", &n);
		F(i, n) scanf("%lf", &vn[i]);
		F(i, n) scanf("%lf", &vk[i]);
		sort(vn, vn + n);
		sort(vk, vk + n);
		int ans1 = 0, ans2 = 0;
		for(int i = n - 1, j = n - 1; i >= 0 && j >= 0; ) {
			if(vn[i] > vk[j]) ans1++, i--;
			else if(vn[i] < vk[j]) i--, j--;
		}
		for(int i = 0, j = 0; i < n && j < n; ) {
			if(vn[i] > vk[j]) ans2++, i++, j++;
			else if(vn[i] < vk[j]) i++;
		}
		printf("Case #%d: %d %d\n", tc + 1, ans2, ans1);
	}
	return 0;
}