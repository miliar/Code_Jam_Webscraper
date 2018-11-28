#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
int itr=0;
while(itr<t)
	{itr++;
	
	 double c,f,x;
	 scanf("%lf %lf %lf",&c,&f,&x);
	 
	 double pres=2;
	 double answer=x/pres;
	 int level=1;
	 if(x<=c)
	 	{
	 	 answer=x/2.0;
	 	}
	 	else
	 while(1)
	 	{
	 	 double dummy=0;
	 	 
	 	 for(int i=0;i<level;i++)
	 	 	{
	 	 	 dummy+=c/(2.0+i*f);
	 	 	}
		 dummy+=x/(2.0+level*f);
		 level++;
		 if(dummy<=answer)
		 	{
		 	 answer=dummy;
		 	}
		 else
		 	{
		 	 break;
		 	}
		 }
	 	printf("Case #%d: ",itr);

		 printf("%0.7lf",answer);
		printf("\n");
	
		}
	
	}

