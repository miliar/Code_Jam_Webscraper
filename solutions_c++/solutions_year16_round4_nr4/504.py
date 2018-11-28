#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

char a[33][33];
int n;
int dp[4][1<<4];
int p[33];
int b[33][33];

int calc(int pos, int mask){
	if (pos == n) return 1;
	int &res = dp[pos][mask];
	if (res != -1) return res;
	res = 1;
	int I = p[pos];
	bool ok = false;
	for (int i=0;i<n;i++){
		if (mask&(1<<i)) continue;
		if (b[I][i]){
			res &= calc(pos+1, mask|(1<<i));
			ok = true;
		}
	}
	if (!ok) res = 0;
	return res;
}

void solve(){
	scanf("%d\n", &n);
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			scanf("%c", &a[i][j]);
		}
		scanf("\n");
	}

	int mini = inf;
	for (int mask=0;mask<(1<<(n*n));mask++){
		int cost = 0;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (a[i][j] == '0'){
					b[i][j] = 0;
				}
				else {
					b[i][j] = 1;
				}

				if (mask&(1<<(i*n + j))){
					if (b[i][j] == 0) cost++;
					b[i][j] = 1;
				}
			}
		}		
		for (int i=0;i<n;i++) p[i] = i;
		bool ok = true;
		do {
			memset(dp, -1, sizeof(dp));
			ok &= calc(0, 0);
		}while(next_permutation(p, p + n));
		if (ok) mini = min(mini, cost);
	}
	cout <<mini<<endl;
}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    int T;
    scanf("%d\n", &T);

    for (int i=0;i<T;i++){
    	printf("Case #%d: ", i+1);
    	solve();
    }


    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
