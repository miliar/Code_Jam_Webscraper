#include <bits/stdc++.h>
using namespace std;

typedef long long          	ll;
typedef long long unsigned 	llu;
typedef double             	dl;
typedef pair<int,int>      	pii;
typedef pair<ll,ll>     	pll;
typedef vector<int>        	vi;
typedef map<int,int> 		mii;
typedef map<ll,ll>         	mll;
typedef map<string,int>    	msi;
typedef map<char,int>      	mci;

#define PI  		acos(-1.0)
#define sn	    	second
#define fs 	    	first
#define pb	    	push_back
#define mp	    	make_pair
#define zero(a) 	memset(a,0,sizeof a)
#define minus(a) 	memset(a,-1,sizeof a)
#define setinf(a) 	memset(a,126,sizeof a)
#define FR(i,x,y) 	for(int i=x;i<=y;i++)
#define FRV(i,x,y) 	for(int i=x;i>=y;i--)
#define all(v)		(v.begin(),v.end())
#define vsort(v)	sort(all(v))
#define nl  		puts("")
#define tcase(cs) 	printf("Case %lld:",++cs)
#define endl		'\n'
#define I_O	    	ios_base::sync_with_stdio(0); cin.tie(0);

int ts,cs=0,mx,ans,sm;
string ss;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>ts;
	while(ts--){
		cin>>mx>>ss;
		ans=0;
		sm=ss[0]-'0';
		for(int i=1;i<=mx;i++){
			if(i>sm){
				ans+=i-sm;
				sm+=(i-sm);
			}
			sm+=(ss[i]-'0');
		}
		cout<<"Case #"<<++cs<<": "<<ans<<endl;
	}
	return 0;
}
