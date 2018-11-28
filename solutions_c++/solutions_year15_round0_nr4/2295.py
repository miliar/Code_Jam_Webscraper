#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <cstring>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
int main()
{
	int t,x,r,c;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&x);
		scanf("%d",&r);
		scanf("%d",&c);
		printf("Case #%d: ",i);
		if(x==1)
		{
			printf("GABRIEL\n");
		}
		else if(x==2)
		{
			if(((r*c)%2)==0)
			{
				printf("GABRIEL\n");
			}
			else
			{
				printf("RICHARD\n");
			}
		}
		else if(x==3)
		{
			if(min(r,c)>1)
			{
				if((r*c)%3==0)
				{
					printf("GABRIEL\n");
				}
				else
				{
					printf("RICHARD\n");
				}
			}
			else
			{
				printf("RICHARD\n");
			}
		}
		else
		{
			if(max(r,c)==4 && min(r,c)>=3)
			{
				printf("GABRIEL\n");
			}
			else
			{
				printf("RICHARD\n");
			}
		}
	}
	return 0;
}