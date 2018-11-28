#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		int x,row,colunm;
		
//		scanf("%d %d %d",&x,&row,&colunm);
		cin>>x>>row>>colunm;
		printf("Case #%d: ",i);

		if(x==1)
			printf("GABRIEL\n");
		else if(x==2)
		{
			if(!(row%2==0 || colunm%2==0))
				printf("RICHARD\n");
			else
				printf("GABRIEL\n");
		}
		else if(x==3)
		{
			if(!(row==2 && colunm==2))
			{
			if(((row==3 || row==2) && (colunm==2 || colunm==3)) || (row==3 && colunm==4) || (row==4 && colunm==3))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
			}
			else
				printf("RICHARD\n");
		}
		
		else if(x==4)
		{
			if(!(row==3 && colunm==3))
			{
			if((row==3 || row==4) && (colunm==3 || colunm==4))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
			}
			else
				 printf("RICHARD\n");

		}
	}
	return 0;
}
