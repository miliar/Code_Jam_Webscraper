#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int lli;
#define modfun 1000000007
#define inf 2147483647
#define MAXN 100005
#define wez(n) int (n); scanf("%d",&(n));
#define debug(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define checkbit(n,b)                ( (n >> b) & 1)

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int((a).size())
#define fill(a,v)                    memset(a, v, sizeof a)
#define rep(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin();!= (c).end(); i++)
int main()
{
	freopen("A-large.in","r",stdin);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int smax;
		cin>>smax;
		string in;
		cin>>in;
		int arr[MAXN];
		int n=in.length();
		for(int i=0;i<n;i++)
			arr[i]=in[i]-'0';
		int ans=0;
		int buffer=0;
		for(int i=0;i<n;i++)
		{
			if(buffer<0 and arr[i]>0)
			{
				ans+=abs(buffer);
				buffer=0;
			}
			buffer+=arr[i];
			buffer--;
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}