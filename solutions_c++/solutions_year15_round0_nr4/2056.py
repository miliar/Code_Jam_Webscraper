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





int main()
{
	int i,j,k,t,r,a,b,c,x,y,z,nc;
//	freopen ("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	sf(nc);
	for(t=1;t<=nc;t++)
	{
		sf(x); sf(r); sf(c);
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",t);
			continue;
		}
		
		if((r*c)%x!=0)
		{
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(min(r,c)<x/2)
		{
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(x>max(r,c))
		{
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(x>=7)//bec hole exists
		{
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		
		else if(x>=min(r,c)+2)
		{
			printf("Case #%d: RICHARD\n",t);
		}
		
		else
		{
			printf("Case #%d: GABRIEL\n",t);
			continue;
		}
		
		
		
	}





	return 0;
}

