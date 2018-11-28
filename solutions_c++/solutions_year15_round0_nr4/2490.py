#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int x,r,c;
	for(int i=0;i<t;i++)
	{
		
		cin>>x>>r>>c;

		if((r*c)%x!=0)
		{
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		if(x==4 && min(r,c)<3)
		{
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		if(x==3 && min(r,c)<2)
		{
			printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		
		printf("Case #%d: GABRIEL\n",i+1);
	}
	return 0;
}
