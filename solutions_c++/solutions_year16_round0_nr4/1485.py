/*
=================================================
   Author : Rohit Sharma
   Handle : skyrohithigh
   Heritage Institute of Technology
   Problem : Fractiles
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

void fractiles(int s, int e){
    string result = "";
    for (int i = s; i < e; i++) {
        result += std::to_string(i)+" ";
    }
    cout<<result<<endl;
}

void solve(){
	ll k, c, s;
	cin>>k>>c>>s;
	if (k == 1) {
        cout<<"1"<<endl;
    }
    else if (c == 1) {
        if (s < k) {
            cout<<"IMPOSSIBLE"<<endl;
        } else {
            fractiles(1, k + 1);
        }
    }
    else if (s < k - 1) {
        cout<<"IMPOSSIBLE"<<endl;
    }else {
        fractiles(2, k + 1);
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
