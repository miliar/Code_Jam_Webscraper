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
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

int n, k;
vector<pair<int, vector<int> > > ans;
vector<int> cur;
int t;
ll a[15];

void check(int mask){
	for(int j = 2; j<=10; j++){
		a[j] = 0;
	}
	for(int i = 0; i<n;i++){
		for(int j = 2; j<11; j++){
			if(mask & (1<<i)){
				a[j] = a[j] * j + 1;
			}
			else a[j] *= j;
		}
	}
	for(int i = 2; i<=10; i++){
		for(int j = 2; j < 100000 && j < a[i]; j++){
			if(a[i] % j == 0){
				cur.pb(j);
				break;
			}
		}
	}
}
void solve(){
	scanf("%d %d", &n, &k);
	ans.clear();
	for(int i=1; ans.size() < k && i<(1<<n); i++){
		if(i&1){
			if(i&(1<<(n-1))){
				cur.clear();
				check(i);
				if(cur.size() == 9) ans.pb(mp(i, cur));
			}
		}
	}
	for(int i = 0;i < k; i++){
		for(int j = 0; j < n; j++){
			if(ans[i].f & (1<<j)) printf("1");
			else printf("0");
		}
		for(int j= 0; j< ans[i].s.size(); j++){
			printf(" %d", ans[i].s[j]);
		}
		printf("\n");

	}

}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif
    scanf("%d", &t);
    for(int i=0;i<t;++i){
    	printf("Case #%d: \n", i+1);
    	solve();
    }




    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}


