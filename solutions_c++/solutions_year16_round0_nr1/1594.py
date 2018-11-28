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
int a[1000001][10];
int ans[1000001];
int main() {
	// your code goes here
	a[0][0]=1;
	int m = 0;
	for(int i=1;i<=1000000;++i) {
		
		repi(j,1,100) {
			int x = i*j;
			while(x) {
				int dig = x%10;
				a[i][dig]=1;
				x/=10;
			}
			bool can = true;
			repi(k,0,10) can = can&a[i][k];
			if(can) {
				ans[i]=j*i;
				m = max(m,j);
		//		if(j==72) cout<<i<<endl;
				break;	
			}
		
		}
		bool can = true;
		repi(k,0,10) can = can&a[i][k];
		if(can) continue;
		cout<<i<<endl;
	}
	int t;
	cin>>t;
	for(int tt=1;tt<=t;++tt) {
		int x;
		cin>>x;
		cout<<"Case #"<<tt<<": ";
		if(x==0) cout<<"INSOMNIA"<<endl;
		else cout<<ans[x]<<endl;
	}
	return 0;
}