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


int t, n;
ll get(ll x, int mask){
	ll y = x;
	while(y > 0){
		mask |= (1<<(y%10));
		y/=10;
	}
	if(mask == (1<<10) - 1) return x;
	return get(x+n, mask);
}
void solve(){
	scanf("%d", &n);
	if(n){
		printf("%lld\n", get(n, 0) );
	}
	else {
		printf("INSOMNIA\n");
	}
}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    int t;
    scanf("%d", &t);
    for(int i = 0;i<t;i++){
    	printf("Case #%d: ", i+1); 
    	solve();
    }




    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}


