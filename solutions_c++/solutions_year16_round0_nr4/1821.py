#include<bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define eps 1e-9
#define sqr(x) ((x)*(x))
#define SET(a,b) memset((a),(b),sizeof((a)))
#define pw(x) (1ll<<(x))
#define buli(x) __builtin_popcountll(x)
#define endl "\n"

const int MOD = 1e9+7;

typedef long long ll;
typedef vector<int> vi;
typedef map<int,int> mii;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

inline bool EQ(double a,double b) { return fabs(a - b) < 1e-9; }
inline void set_bit(int & n, int b) { n |= pw(b); }
inline void unset_bit(int & n, int b) { n &= ~pw(b); }

inline void check(ll &x) {
	if(x>=MOD)
		x%=MOD;
}

int main() {
	freopen("TASK.in","r",stdin);	
	freopen("TASK.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<tt<<": ";
		for(int i=1;i<=s;i++) {
			if(i!=1) cout<<" ";
			cout<<i;
		}
		cout<<endl;
	}
	return 0;
}