#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = 1E9;	
const int MAXN = 222;

int tt, n, k;
int id[MAXN];
ld p[MAXN], ans;
ld dp[MAXN][MAXN];

int main() {
	
	cin >> tt;
	forn(ttt, tt) {
		cin >> n >> k;
		printf("Case #%d: ", ttt + 1);

		forn(i, n)
			cin >> p[i];
	    sort(p, p + n);
	    ans = 0;
	    
		for (int L = 0; L <= k; L++) {
			int ptr = 0;
			forn(j, L)	
				id[ptr++] = j;
			int j2 = n - 1;
			while (ptr != k) {
				id[ptr++] = j2;
				j2--;
			}
						
			memset(dp, 0, sizeof(dp));	
			
			dp[0][0] = 1.0;
			for (int i = 0; i < k; i++)
				for (int j = 0; j <= k; j++) {
					dp[i + 1][j] += dp[i][j] * p[id[i]];
					dp[i + 1][j + 1] += dp[i][j] * (1.0 - p[id[i]]);
				}
				
			ld curAns = dp[k][k / 2];
			if (curAns > ans)
				ans = curAns;
		}
		
		cout.precision(30);
		cout << ans << '\n';
	}
		
	return 0;
}                