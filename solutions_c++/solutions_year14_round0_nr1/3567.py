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
	
	 int n;
	 scanf("%d",&n);
	 bool flag[17]={0};
	 for(int i=0;i<4;i++)
	 	{
	 	for(int j=0;j<4;j++)
	 		{
	 		 int a;
	 		 scanf("%d",&a);
	 		 if(i==n-1)
	 		 	{
	 		 	 flag[a]=1;
	 		 	}
	 		}
	 	}
	 scanf("%d",&n);
	 int count=0;
	 int ans=0;
	 for(int i=0;i<4;i++)
	 	{
	 	for(int j=0;j<4;j++)
	 		{
	 		 int a;
	 		 scanf("%d",&a);
	 		 if(i==n-1)
	 		 	{
	 		 	 if(flag[a]==1)
	 		 	 	{
	 		 	 	 count++;
	 		 	 	 ans=a;
	 		 	 	}
	 		 	}
	 		}
	 	}
	 	printf("Case #%d: ",itr);
	if(count==1)
		{
		 printf("%d",ans);
		}
	else if(count==0)
		{
		 printf("Volunteer cheated!");
		}
	else
		{
		 printf("Bad magician!");
		}
	printf("\n");
	}
}
