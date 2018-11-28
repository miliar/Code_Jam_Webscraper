/*
=================================================
   Author : Rohit Sharma
   Handle : skyrohithigh
   Heritage Institute of Technology
   Problem : Coin Jam
   Contest : CodeJam16
   Website : Google
   Date : 09/04/2016
=================================================
 */
#include <bits/stdc++.h>
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define INF INT_MAX
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define DEBUG(X) cout<<#X<<" : "<<X<<endl;
using namespace std; 
typedef vector<int> vint;
typedef vector<long long int> vll;
typedef vector<bool> vbl;
typedef vector<vector<int> > vvint;
typedef vector<vector<long long int> > vvll;
typedef pair<int,int> pint;
typedef pair<long long int, long long int> pll;
typedef long long int ll;
/* ========== END OF TEMPLATE ===========*/
ll coin[33];
ll n,  j;

void printCoin(){
	for(int i=n-1; i >= 0 ; i--){
		cout<<coin[i];
	}
	cout<<" ";
}

void next(){
	for(int i=1; i < n; i++){
		if(coin[i] == 0){
			coin[i] = 1;
			for(int k=i-1; k > 0; k--){
				coin[k] = 0;
			}
			break;
		}
	}
}

ll inBaseX(ll x){
	ll num = 0;
	ll term = 1;
	for(int i=0; i < n; i++){
		if(coin[i] == 1){
			num += term;
		}
		term = term*x;
	}
	return num;
}

ll firstNontrivalDivisor(ll n) {
	ll root = sqrt(n+1);
    for (ll i = 2; i <= root; i++) {
        if (n % i == 0) {
            return i;
        }
    }
    return -1;
}


void solve(){
	cout<<endl;
	cin>>n>>j;
	coin[0] = 1;
	coin[n-1] = 1;
	for(int i=1; i <= j;){
		//all bases
		vll ans;
		bool flag = true;
		for(int b = 2; b <= 10; b++){
			ll divisor = firstNontrivalDivisor(inBaseX(b));
			if(divisor == -1){
				flag = false;
				break;
			}else{
				ans.pb(divisor);
			}
		}
		if(flag){
			printCoin();
			for(int k=0; k < 9; k++){
				cout<<ans[k]<<" ";
			}
			cout<<endl;
			i++;
		}
		ans.clear();
		next();
	}
}

int main(void){
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	// freopen("input.txt","r",stdin);
	ll t = 1;
	cin>>t;
	for(int i=1; i <= t; i++){
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}

/* ======================== END OF PROGRAM ===================== */
