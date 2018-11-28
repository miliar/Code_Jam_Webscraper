#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)
#define pr(a) printf("%d",a)
#define prn(a) printf("%d\n",a)
#define scll(a) scanf("%lld",&a)
#define prll(a) printf("%lld",a)
#define prlln(a) printf("%lld\n",a)
typedef long long LL;
int t;
int main() {
	// your code goes here
	
	int t;
	cin>>t;
	for(int tt=1;tt<=t;++tt) {
		cout<<"Case #"<<tt<<": ";
		int k,c,s;
		cin >>k >>c >>s;
		LL kcm = 1;
		for(int p = 1; p<c; ++p) kcm *= k;
		if((c==1 && s<k) || s < (k+1)/2) {
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		} else if(c==1) {
			for(int i=1;i<=k;++i) cout<<i<<" ";
			cout<<endl;
			continue;
		}
		for(int i = 0; i<(k)/2; ++i) {
			cout<<2*i*kcm + (i+1)*2<<" ";
		}
		if(k%2 == 1) {
			cout<<kcm*k<<" ";
		}
		
		cout<<endl;
	}
	return 0;
}