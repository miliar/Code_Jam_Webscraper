
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;

#define read(x) freopen(x,"r",stdin)
#define write(x) freopen(x,"w",stdout)
#define REP(i,n) for( i=0;i<(n);i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define FOR(i,a,b) for( i=(a);i<=(b);i++)
#define FORD(i,a,b) for( i=(a);i>=(b);i--)
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define ins insert

typedef pair<int,int> pii;
typedef vector<ll> vi;
typedef vector<pii> vpii;
// Backspace...
int main(){
	read("B-large.in");
	write("output1.in");
	ll x=1,t,i,j;
	char s[101010];
	cin>>t;
	list<char> l;
	while(t--){
		l.clear();
		cin>>s;
		i=strlen(s)-1;
		while(s[i]!='-' && i>=0) i--;
		while(i>=0){
			l.pb(s[i]);
			i--;
		}
		l.unique();
		cout<<"Case #"<<x<<": "<<l.size()<<endl;
		x++;
	}
    return 0;
}
