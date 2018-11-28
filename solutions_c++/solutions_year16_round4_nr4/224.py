#include<time.h>
#include<stdlib.h>
#include<assert.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<map>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define rep(i,l,r) for(int i=l;i<r;i++)
#define abs(x) ((x)<(0)?(-x):(x))
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define de(x) cout << #x << " = " << x << endl;
#define local(x) freopen(x".in", "r", stdin);
#define setIO(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout);
const int N = 101010;
int n, vis[N], flag[N], cnt[100000], i, j, ii, o;
char ch[10][10];
int check(int x, int y) {
	int i, j, ans = 1;
	if (x == n)
		return 1;
	for (i = 0; i < n; i++)
		if (!vis[i]) {
			vis[i] = 1;
			int Flag = 0;
			for (j = 0; j < n; j++)
				if ((!flag[j]) && (((1 << (i * n + j)) | y) == y)) {
					Flag = 1;
					flag[j] = 1;
					ans = (ans & check(x + 1, y));
					flag[j] = 0;
				}
			ans = (ans & Flag);
			vis[i] = 0;
		}
	return ans;
}
int main() {
	setIO("D-small-attempt0");
	int test;
	scanf("%d", &test);
	for (i = 1; i <= 70000; i++)
		cnt[i] = cnt[i - (i & -i)] + 1;
	for (ii = 1; ii <= test; ii++) {
		scanf("%d", &n);
		o = 0;
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++) {
				scanf(" %c", &ch[i][j]);
				if (ch[i][j] == '1')
					o |= (1 << (i * n + j));
			}

		int ans = 0x37373737;
		for (i = 0; i < (1 << (n * n)); i++)
			if ((i | o) == i) {
				if (check(0, i))
					ans = min(ans, cnt[i] - cnt[o]);
			}
		printf("Case #%d: ", ii);
		printf("%d\n", ans);
	}
}
