#include<stdlib.h>
#include <stdio.h>
#include<iostream>
using namespace std;
int main(void)
{


	int i,j,a[4],b[4],n,m,t,l,count,bin,p;




	scanf("%d",&t);

	for(l=1;l<=t;l++)
	{
		count=0;

		scanf("%d",&n);

		for(i=1;i<=4*(n-1);i++)
		scanf("%d",&bin);

		for(i=1;i<=4;i++)
		scanf("%d",&a[i]);

		for(i=1;i<=4*(4-n);i++)
		scanf("%d",&bin);



		scanf("%d",&m);

		for(i=1;i<=4*(m-1);i++)
		scanf("%d",&bin);

		for(i=1;i<=4;i++)
		scanf("%d",&b[i]);

		for(i=1;i<=4*(4-m);i++)
		scanf("%d",&bin);

		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
                 if(a[i]==b[j])
				{
					count++;
					p=a[i];
				}
			}
		}


	if(count==1)
	printf("Case #%d: %d\n",l,p);

	else if(count>1)
	printf("Case #%d: Bad magician!\n",l);

	else if(count==0)
	printf("Case #%d: Volunteer cheated!\n",l);

	}

	return 0;
}
