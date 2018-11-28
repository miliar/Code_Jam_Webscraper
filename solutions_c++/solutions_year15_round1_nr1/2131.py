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


int arr[1008]={0};


int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,ans1,ans2,temp;
	freopen ("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	sf(z);
	for(t=1;t<=z;t++)
	{
		sf(n);
		ans1=0;ans2=0;
		temp=0;//mx slope
		for(i=1;i<=n;i++)
		{
			sf(arr[i]);
			if(i!=1 && arr[i]<arr[i-1])
			{
				ans1+=arr[i-1]-arr[i];
			}
			
		}
		for(i=1;i<=n;i++)
		{
			if(i!=1 && arr[i]<arr[i-1])
			{
				//ans1+=arr[i-1]-arr[i];
				temp=max(temp,arr[i-1]-arr[i]);
			}
		}
		for(i=1;i<=n;i++)
		{
			if(i==n)
			continue;
			ans2+=min(arr[i],temp);
			
			
		}
		printf("Case #%d: %d %d\n",t,ans1,ans2);
		
	}





	return 0;
}

