/*
=================================================
   Author : Rohit Sharma
   Handle : skyrohithigh
   Heritage Institute of Technology
   Problem : Counting Sheep
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

void solve(){
	ll n;
	cin>>n;
	if(n == 0){
		cout<<"INSOMNIA"<<endl;
		return;
	}
	ll num, i;
	set<int> digits;
	for(i=1;  ; i++){
		num = i * n;
		while(num > 0){
			digits.insert(num%10);
			num /= 10;
		}
		if(digits.size() >= 10) break;
	}
	cout<<(i*n)<<endl;
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
