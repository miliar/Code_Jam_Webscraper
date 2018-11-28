#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define N 10000000
int sum[N+10];
bool check(int s)
{
	int i,j;
	char str[20];	
	sprintf(str, "%d", s);
	j=strlen(str)-1;
	for(i=0;i<j;i++,j--)
		if(str[i]!=str[j])
			return 0;
	return 1;
}

bool cc(long long s)
{
	int i,j;
	char str[20];	
	sprintf(str, "%I64d", s);
	j=strlen(str)-1;
	for(i=0;i<j;i++,j--)
		if(str[i]!=str[j])
			return 0;
	return 1;
}
int main()
{
	int t,test=0,i,aa,bb;
    long long tmp,a,b;
	for(i=1;i<=N;i++)
	{
		sum[i]=sum[i-1];
		if(check(i))
		{
			tmp=i*i;
			if(cc(tmp))
				sum[i]++;
		}
	}
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("2s.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld%lld",&a,&b);
		aa=sqrt(a);
		if((long long)aa*aa==a)
			aa--;
		bb=sqrt(b);
		printf("Case #%d: %d\n",++test,sum[bb]-sum[aa]);
	}

	return 0;
}