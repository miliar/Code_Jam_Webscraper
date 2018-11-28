#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc,x,rc,cr,r,c,k;
	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);
	cin>>tc;
	for(k=1;k<=tc;k++)
	{
		cin>>x>>rc>>cr;
		r=max(cr,rc);
		c=min(cr,rc);
		if(r>=x&&c>=(x-1))
		{
			if(((r-x)*c)%x==0)
				printf("Case #%d: GABRIEL\n",k);
			else
				printf("Case #%d: RICHARD\n",k);
		}
		else
			printf("Case #%d: RICHARD\n",k);

	}
	return 0;
}
