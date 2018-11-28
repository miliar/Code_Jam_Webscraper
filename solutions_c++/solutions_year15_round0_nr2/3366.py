#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int lli;
#define modfun 1000000007
#define inf 2147483647
#define MAXN 1005
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
	freopen("B-large.in","r",stdin);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int d;
		cin>>d;
		vector<int> arr;
		int ans=0,tim=0;
		for(int i=0;i<d;i++){
			int te;
			cin>>te;
			arr.push_back(te);
			ans=max(ans,arr[i]);
		}
		if(ans<4)
			cout<<"Case #"<<test<<": "<<ans<<endl;
		else
		{
			sort(arr.rbegin(),arr.rend());
			for(int i=2;i<=1000;i++)
			{
				int tem=0;
				rep(j,sz(arr))
				{
					if(arr[j]>i)
					{
						tem+=((arr[j]-1)/i);
					}
				}
				ans=min(ans,tem+i);
			}
			cout<<"Case #"<<test<<": "<<ans<<endl;
		}
	}
	return 0;
}