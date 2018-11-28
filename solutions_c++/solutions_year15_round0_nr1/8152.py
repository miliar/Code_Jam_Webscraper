#include<stdio.h>
int input()
{
    int t=0;
    char ch=getchar();
    while(ch<33)
    ch=getchar();
    while(ch>33)
    {
        t=(t<<3)+(t<<1)+ch-'0';
        ch=getchar();
    }
    return t;
}
int main()
{
	int t,n,i,j;
	long long sum,count;
	char ch;
	int A[1003];
	t=input();
	for(j=0;j<t;j++)
	{
		n=input();
		count=0;
		for(i=0;i<=n;i++)
		{
			ch=getchar();
			A[i]=ch-'0';
		}
		sum=A[0];
		for(i=1;i<=n;i++)
		{
			if(A[i]&&i<=sum)
			{
				sum+=A[i];
			}
			else if(A[i]&&i>sum)
			{
				count+=(i-sum);
				sum=i+A[i];
			}
		}
		printf("Case #%d: %lld\n",j+1,count);
	}
	return 0;
}
