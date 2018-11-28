#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	int t,x,r,c;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
		cin>>x>>r>>c;
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",l);
		}
		else if(x==2)
		{
			if(r*c<x||(r*c)%2)
				printf("Case #%d: RICHARD\n",l);
			else
				printf("Case #%d: GABRIEL\n",l);
		}
		else if(x==3)
		{
			if(r==3&&c==3||r==3&&c==4||r==4&&c==3||r==2&&c==3||r==3&&c==2)
				printf("Case #%d: GABRIEL\n",l);
			else
				printf("Case #%d: RICHARD\n",l);
		}
		else if(x==4)
		{
			if(r==4&&c==4||r==3&&c==4||r==4&&c==3)
				printf("Case #%d: GABRIEL\n",l);
			else
				printf("Case #%d: RICHARD\n",l);
		}
	}
	return 0;
}