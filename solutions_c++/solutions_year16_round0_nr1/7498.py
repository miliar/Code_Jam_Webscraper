
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
	read("A-large.in");
	write("my.out");
	ll x,t,chk,tmp,k,i,j,n;
	cin>>t;
	x=1;
	while(t--){
		cin>>n;
		chk=0;
		i=2;
		if(n==0){
			cout<<"Case #"<<x<<":"<<" INSOMNIA"<<endl;
			x++;
			continue;
		}
		j=n;
		while(__builtin_popcount(chk)!=10){
			tmp=n;
			while(tmp){
				k=(tmp%10);
				chk |= 1<<k;
				if(__builtin_popcount(chk)==10)
					break;
				tmp/=10;
			}
			if(__builtin_popcount(chk)==10)
				break;
			n=j*i;
			i++;
		}
		cout<<"Case #"<<x<<": "<<n<<endl;
		x++;
	}
    return 0;
}
