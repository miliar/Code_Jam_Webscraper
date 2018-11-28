#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		int n;string s;
		cin>>n>>s;

		int ans=0,cnt=0;
		for(int i=0;i<=n;++i){
			if(cnt<i)ans+=(i-cnt),cnt=i;
			cnt+=(s[i]-'0');
		}

		cout<<"Case #"<<++cs<<": "<<ans<<"\n";
	}
	return 0;
}
