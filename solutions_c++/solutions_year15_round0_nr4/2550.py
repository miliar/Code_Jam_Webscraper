#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int x,r,c,temp,res;
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",i);
		temp=r*c;
		if(x==1)
			res=1;
		else if(x==2)
		{
			if(temp%2==0)
				res=1;
			else
				res=0;
		}
		else if(x==3)
		{
			if(temp==6||temp==9||temp==12)
				res=1;
			else
				res=0;
		}
		else
		{
			if(temp==12||temp==16)
				res=1;
			else
				res=0;
		}
		if(res==0)
			printf("RICHARD\n");
		else
			printf("GABRIEL\n");
	}
	return 0;
}

