#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007
#define UPD(a,b) { a = max(a,b); }

int f[111][1111];
int P,Q,n;
int H[MaxN],G[MaxN],Times[MaxN];
int main() {
	freopen("input.txt","r",stdin);// freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) {
		printf("Case #%d: ", TTT);
		cin >> P >> Q >> n;
		For(i,1,n) scanf("%d%d",&H[i],&G[i]);
		int sum = 0;
		For(i,1,n) sum += G[i];
		Fill(f,-INF);
		f[0][1] = 0;
		For(i,0,n - 1) {
			int nnd = 0;
			For(k,0,H[i + 1] / P) {
				if ((H[i + 1] - k * P) % Q <= P && ((H[i + 1] - k * P) % Q != 0 || H[i + 1] - k * P == 0)) {
					nnd = k; break ;
				}
				++nnd;
			}
			int tmp = (H[i + 1] - nnd * P) / Q;
			For(cand,0,1000) if (f[i][cand] >= 0) {
				UPD(f[i + 1][cand + H[i + 1]/ Q + (H[i + 1] % Q != 0)],f[i][cand]);
				if (H[i + 1] - nnd * P <= 0) {
					if (cand - nnd >= 0) UPD(f[i + 1][cand - nnd],f[i][cand] + G[i + 1]);
					continue ;
				}
				if (cand + tmp - nnd - 1 >= 0) UPD(f[i + 1][cand + tmp - nnd - 1], f[i][cand] + G[i + 1]);
			}
		}
		int ans = 0;
		For(rem,0,1000) UPD(ans,f[n][rem]);
		cout << ans << endl;
	}
	return 0;
}

