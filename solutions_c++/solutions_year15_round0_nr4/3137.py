#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define lldd long long int
#define mod 1000000007
using namespace std;
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tt=t;
	while(t--)
	{
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		int mini  = min(r,c);
		int maxi = max(r,c);
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",tt-t);
		}
		else if(x==2)
		{
			if(mini==1 && maxi==1)
				printf("Case #%d: RICHARD\n",tt-t);
			else if(mini==1 && maxi==3)
				printf("Case #%d: RICHARD\n",tt-t);
			else if(mini==3 && maxi==3)
				printf("Case #%d: RICHARD\n",tt-t);
			else
				printf("Case #%d: GABRIEL\n",tt-t);
		}
		else if(x==3)
		{
			if(mini==2 && maxi ==3)
				printf("Case #%d: GABRIEL\n",tt-t);
			else if(mini==3 && maxi==3)
				printf("Case #%d: GABRIEL\n",tt-t);
			else if(mini==3 && maxi==4)
				printf("Case #%d: GABRIEL\n",tt-t);
			else
				printf("Case #%d: RICHARD\n",tt-t);
		}
		else if(x==4)
		{
			if((mini==4 || mini==3) && maxi==4)
				printf("Case #%d: GABRIEL\n",tt-t);
			else
				printf("Case #%d: RICHARD\n",tt-t);
		}
	}
}
