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

int N, K;
double a[202];
double dp[202][202];
bool calced[202][202];
vector < double > v;

double calc(int pos, int t){
	if (pos == K){
		if (t == K/2) return 1.0;
		return 0.0;
	}
	double &res = dp[pos][t];
	if (calced[pos][t]) return res;
	calced[pos][t] = true;
	res = calc(pos+1, t+1)*v[pos] + calc(pos+1, t)*(1.0 - v[pos]);
	return res;
}

void solve(){
	scanf("%d%d", &N, &K);
	for (int i=0;i<N;i++){
		cin >>a[i];
	}
	sort(a, a + N);
	double maxi = 0.0;
	for (int i=0;i<N;i++){
		v.clear();
		for (int j=0;j<K;j++){
			v.pb(a[(i+j)%N]);
		}
		memset(calced, 0, sizeof(calced));
		maxi = max(maxi, calc(0, 0));
	}
	printf("%.10f\n", maxi);
}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);

    for (int i=0;i<T;i++){
    	printf("Case #%d: ", i+1);
    	solve();
    }


    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
