#include <stdio.h>
#include <math.h>

bool ispal(int n)
{
	char a[10];
	int i=0, j;
	j=sprintf(a,"%d",n)-1;
	while(i<j)
	{
		if(a[i++]!=a[j--]) return false;
		
	}
	return true;
}

int main()
{
	int T,C=1;
	int A,B,count,i,l1,l2;
	scanf("%d",&T);
	while(T--)
	{
		count=0;
		scanf("%d %d",&A,&B);
		l1=ceil(sqrt(A));
		l2=sqrt(B);
		for(i=l1;i<=l2;i++)
		{
			if(ispal(i) && ispal(i*i)) count++;
		}
		printf("Case #%d: %d\n",C++,count);
	}
	return 0;
}
