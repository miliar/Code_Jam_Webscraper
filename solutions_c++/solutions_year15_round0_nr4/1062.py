#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,x,r,c;
	scanf("%d", &t);
	bool flag;
	for(int i=1; i<=t; i++)
	{
		scanf("%d %d %d", &x, &r, &c);
		if((r*c)%x!=0)
		flag=false;
		else if(x==1)
		flag=true;
		else if(x==2)
		{
			if(r%2==0 || c%2==0)
			flag=true;
			else
			flag=false;
		}
		else if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))
			flag=true;
			else
			flag=false;
		}
		else if(x==4)
		{
			if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
			flag=true;
			else
			flag=false;
		}
		if(flag)
		printf("Case #%d: GABRIEL\n", i);
		else
		printf("Case #%d: RICHARD\n", i);
	}
}
