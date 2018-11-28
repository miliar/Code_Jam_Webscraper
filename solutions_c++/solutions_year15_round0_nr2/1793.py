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
int p[1005];
int dp[1005];
int main()
{
	freopen("inp.in", "r", stdin);
     	freopen("out.txt", "w", stdout);

	int t,d,mx,ans,i,j,rem,cnt;
	cin>>t;
	int k=1;
	while(t--){
		cin>>d;
		mx=0;
		F(i,0,d){
			cin>>p[i];
			mx=max(mx,p[i]+1);
		}

		ans=1001;
		F(i,1,mx){
			cnt=0;
			F(j,0,i+1)dp[j]=0;
			F(j,i+1,1001){
				if(j&1){
					dp[j]=min(dp[(j+1)/2]+dp[j/2]+1,dp[j-i]+1);
				} else {
					dp[j]=min(dp[j/2]+dp[j/2]+1,dp[j-i]+1);
				}
			}
		
			F(j,0,d){
				cnt+=dp[p[j]];
			}

			//cout<<i<<" "<<cnt<<endl;
			ans=min(ans,cnt+i);
		}
		cout<<"Case #"<<k++<<": "<<ans<<endl;
	}
}






