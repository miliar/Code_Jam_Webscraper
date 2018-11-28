// AUTHOR: ARVIND NAIR

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pi;
typedef vector<int> vi;

#define TEST  int test_case; scanf("%d",&test_case); while(test_case--)
#define RT fprintf(stderr, "\nTIME = %lf\n", 1.0 * clock()/CLOCKS_PER_SEC);
#define rep(a,c)   for ( int (a)=0; (a)<(c); (a)++)
#define repn(a,b,c)  for ( int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for (  int (a)=(b); (a)>=(c); (a)--)
#define FOR(arr) for(auto &i:arr)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb push_back
#define mp make_pair
#define EPS (double)(1e-9)
#define MOD 1000000007
#define M(x,i) memset(x,i,sizeof(x))
#define trace(x)    cout<<#x<<" is "<<x<<"\n"
#define sz(x) (int)(x.size())
#define si(n) scanf("%d",&n)
#define gi(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define gll(n) printf("%lld\n",n)

bool seen[10];

bool check(ll x) {

	int p;

	while(x)
		p=x%10,x/=10,seen[p]=1;

	bool ans=true;

	rep(i,10)
	if(!seen[i])
		ans=false;

	return ans;
}

int main() {  

freopen("linp1.in","r",stdin);
freopen("lop1.out","w",stdout); 

int t; si(t);

repn(test,1,t) {

	int n; si(n);
	ll ans=-1;
	M(seen,0);

 if(n==0) {

 	printf("Case #%d: INSOMNIA\n",test);
 	continue;
 }

 repn(i,1,1000000) {

 	ll num=1LL*i*n;

 	if(check(num)) {

 		ans=num;
 		break;
 	}
 }

 if(ans==-1)
 	printf("Case #%d: INSOMNIA\n",test);
 else
 	printf("Case #%d: %lld\n",test,ans);

}
     
return 0;
}
