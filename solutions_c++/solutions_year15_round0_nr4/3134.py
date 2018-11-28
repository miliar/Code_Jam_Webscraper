#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen( "input5.txt" , "r" ,stdin);
	freopen( "output5.txt" , "w" ,stdout);
	int T;
	scanf("%d\n",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		int x,r,c;
		scanf("%d%d%d",&x,&r,&c);
		if(x==1)
		{
			printf("GABRIEL\n");	
		}
		else if(x==2)
		{
			if((r*c)%2==0)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
		else if(x==3)
		{
			if((r*c)%3==0&&(r*c)!=3)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
		else if(x==4)
		{
			if((r*c)>=12)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
	}
	return 0;
}
