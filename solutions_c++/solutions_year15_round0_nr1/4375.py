#include<bits/stdc++.h>
#define ll long long int
#define F first
#define S second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rep(i,in1,n) for(i=in1;i<=n;i++)
#define repd(i,in1,n) for(i=in1;i>=n;i--)

#define pf(n) printf("%d ",n);
#define sf(n) scanf("%d",&n)
#define sl(n) scanf("%I64d",&n)
#define nl printf("\n")
#define mem(arr,init) memset(arr,init,sizeof(arr))
#define vi vector<int>
#define vvi vector<vi>

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define ep emplace_back//c++11
#define ii pair<int,int>
using namespace std;




string str;
int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,nc,ans,sum,smax;
	freopen ("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	sf(nc);
	for(t=1;t<=nc;t++)
	{
		sf(smax);
		cin>>str;
		ans=0;sum=0;
		for(i=0;i<=smax;i++)
		{
			if(i>sum)
			{
				ans+=(i-sum);
				sum+=(i-sum);
				
			}
			sum+=str[i]-'0';
		}
		printf("Case #%d: %d\n",t,ans);
		
		
	}
	





	return 0;
}

