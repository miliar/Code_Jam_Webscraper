#include<iostream>
#include<stdio.h>
#include<cmath>
#include<vector>
using namespace std;
int main()
{
	int t,count=0;
	scanf("%d",&t);
    while(t--)
    {
    	count++;
    	int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		printf("Case #%d: ",count);
		if((r*c)%x!=0)
		{
			cout<<"RICHARD\n";
			continue;
		}
		if(x==1 || x==2)
		{
			printf("GABRIEL\n");
			continue;
		}
		else if(x==3)
		{
			if((r>=3&&c>=2) || (c>=3&&r>=2))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");	
		}
		else if(x==4)
		{
			if((r>=4&&c>=3) || (c>=4&&r>=3))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
	}
	return 0;
}
