#include<cstdio>
#include <algorithm>
using namespace std;

int main()
{
int test,iter,n;
float listA[1005],listB[1005];
int low,high,count;
int i,j;
scanf("%d",&test);

for(iter=1;iter<=test;iter++)
{
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%f",&listA[i]);
   	sort(listA, listA+n);
	for(i=0;i<n;i++)
		scanf("%f",&listB[i]);
	 sort(listB, listB+n);

	low=0,high=n-1;
	count=0;

	for(i=n-1;i>=0;i--)
	{
		if(listA[high]<=listB[i])
		{
			low++;
		}
		else
		{
			high--;
			count++;		
		}
	}
	printf("Case #%d: %d",iter,count);

	low=0,high=n-1;
	count=0;

	for(i=n-1;i>=0;i--)
	{
		if(listA[i]>=listB[high])
		{
			low++;
		}
		else
		{
			high--;
			count++;		
		}
	}

	printf(" %d\n",n-count);

/*
	printf("list is \n");
	for(i=0;i<n;i++)
		printf("%f",listA[i]);

	printf("list is \n");
	for(i=0;i<n;i++)
		printf("%f",listB[i]);
*/
}


return 0;
}
