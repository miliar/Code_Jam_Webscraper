#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const int MAXN = 112;
const int K = 12;

int f[MAXN][MAXN*K];

void up(int &a, int b){
	a = max(a, b);
}

int div1(int a, int b){
	if(a <= 0)
		return 0;
	return (a-1)/b+1;
}

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int i0 = 1;
	int T;
	scanf("%d", &T);
	for (i0 = 1; i0 <= T; i0++) {
		int i, j;
		int n;
		int P, Q;
		scanf("%d%d%d", &P, &Q, &n);
		memset(f, -100, sizeof f);
		f[0][1] = 0;

		for(i = 0; i < n; i++){
			int h, g;
			int t;
			scanf("%d%d", &h, &g);
			t = div1(h, Q);
			for(j = 0; j <= i*K+1; j++)
				up(f[i+1][j+t], f[i][j]);

			j = 1;
			while(true){
				t = div1(h-(j-1)*P, Q);
				if(h-(t-1)*Q-j*P <= 0){
					t = t-1-j;
					break;
				}
				j++;
			}

			for(j = max(0, -t); j <= i*K+1; j++)
				up(f[i+1][j+t], f[i][j]+g);
		}

		int ans = 0;
		for(j = 0; j <= n*K+1; j++)
			up(ans, f[n][j]);


		printf("Case #%d: %d\n", i0, ans);
	}
	return 0;
}
