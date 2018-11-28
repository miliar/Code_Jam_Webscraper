#include <bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)
using namespace std;
int main()
{
	freopen("inp.in", "r", stdin);
     	freopen("out.txt", "w", stdout);

	int t,n,req,curr,ans,i;
	string s;
	int k=1;	
	cin>>t;

	while(t--){
		cin>>n>>s;
		ans=0;
		curr=0;

		F(i,0,n+1){
			req=i;
			if(s[i]!='0' && curr<req){
				ans+=req-curr;
				curr+=req-curr;
			}
			curr+=(s[i]-'0');
			//cout<<i<<" "<<ans<<endl;
		}

		cout<<"Case #"<<k++<<": "<<ans<<endl;
	}
}
