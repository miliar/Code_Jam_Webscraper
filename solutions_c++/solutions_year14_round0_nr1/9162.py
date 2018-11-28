#include<iostream>
//#include<stdio.h>
using namespace std;
int main()
{
int p,t,val,chk=0;
scanf("%d",&t);
for(p=1;p<=t;p++)
{
	chk=0;
	int a[4][4],b[4][4],ra,rb,i,j;
	scanf("%d",&ra);
	for(i=0;i<4;i++)
	    for(j=0;j<4;j++)
	        scanf("%d",&a[i][j]);
	scanf("%d",&rb);
	for(i=0;i<4;i++)
	    for(j=0;j<4;j++)
	        scanf("%d",&b[i][j]);
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a[ra-1][i]==b[rb-1][j])
			{
			val=a[ra-1][i];
			chk++;	
			}
		}
	}
	printf("Case #%d: ",p);
	if(chk==0)
	  printf("Volunteer cheated!");
	else if(chk==1)
	  printf("%d",val);
	else
	  printf("Bad magician!");
	printf("\n");
}
return 0;
     
}
