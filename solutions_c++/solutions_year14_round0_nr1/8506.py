#include<iostream>
#include<stdio.h>
using namespace std;
void program(int no)
{
	int a[20]={0};
	int k,temp,countr=0,last_p,i;
	
	// First matrix
	scanf("%d",&k);
	for(i=0;i<(k-1)*4;i++)
		scanf("%d",&temp);

	for(i=0;i<4;i++)
	{
		scanf("%d",&temp);
		a[temp]++;
	}
	
	for(i=0;i<(4-k)*4;i++)
		scanf("%d",&temp);

	// Second matrix	
	scanf("%d",&k);
	for(i=0;i<(k-1)*4;i++)
		scanf("%d",&temp);

	for(i=0;i<4;i++)
	{
		scanf("%d",&temp);
		a[temp]++;
	}
	
	for(i=0;i<(4-k)*4;i++)
		scanf("%d",&temp);
	
	for(i=1;i<17;i++)
		if(a[i]==2)
		{
			last_p=i;
			countr++;
		}
	if(countr==1)
		printf("Case #%d: %d\n",no,last_p);
	else if(countr>1)
		printf("Case #%d: Bad magician!\n",no);
	else
		printf("Case #%d: Volunteer cheated!\n",no);
}
int main()
{
int t,i;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
program(i);
}
return 0;
}