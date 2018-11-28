/*
=================================================
   Author : Rohit Sharma
   Handle : skyrohithigh
   Heritage Institute of Technology
   Problem : The Last Word
   Contest : CodeJam16
   Website : Google
   Date : 16/04/2016
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
	string s;
	cin>>s;
	string ans = s.substr(0,1);
	for(int i=1; i < s.length(); i++){
		if(s[i] < ans[0]){
			ans = ans + s[i];
		}else{
			ans = s[i] + ans;
		}
	}
	cout<<ans<<endl;
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
