#include <bits/stdc++.h>
using namespace std;
int main() 
{
	int i,j,k,l,n,m,x,r,c,t;
	scanf("%d",&t);
	for(int yu=1;yu<=t;yu++)
	{
		printf("Case %d: ",yu);
		scanf("%d %d %d",&x,&r,&c);
		if(x==1)
			printf("GABRIEL\n");
		else if(x==2)
		{
			l=r*c;
			if(l%2==0)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
		else if(x==3)
		{
			if(r==1 || c==1)
				printf("RICHARD\n");
			else
			{
				l=r*c;
				if(l%3==0)
					printf("GABRIEL\n");
				else
					printf("RICHARD\n");
			}
		}
		else
		{
			if(r==1 || c==1)
				printf("RICHARD\n");
			else
			{
				l=r*c;
				if(l%4==0)
					printf("GABRIEL\n");
				else
					printf("RICHARD\n");
			}
		}
	}
	return 0;
}
