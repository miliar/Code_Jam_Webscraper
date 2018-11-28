#include<stdio.h>
long long aaa[30],ggg[100];
int test(long long x)
{
	long long k=0,i;
	while(x)
	{
		k++;
		aaa[k]=x%10;
		x/=10;
	}
	for(i=1;i<=k;i++)
	{
		if(aaa[i]!=aaa[k+1-i])
		{
			return 0;
		}
	}
	return 1;
}
int main(){
	freopen("input5.in","r",stdin);
	freopen("output.txt","w",stdout);
	long long k,n=0;
	long long T,j,i,A,B,a,b;
	for(k=1;k<=10000000;k++)
	{
		if((test(k)==1)&&(test(k*k)==1))
		{
			n++;
			ggg[n]=k;
		}
	}
	scanf("%I64d",&T);
	for(j=1;j<=T;j++)
	{
		scanf("%I64d%I64d",&A,&B);
		for(k=1;k<=n;k++)
		{
			if(A<=(ggg[k]*ggg[k]))
			{
				a=k;
				break;
			}
		}
		for(k=n;k>=1;k--)
		{
			if(B>=(ggg[k]*ggg[k]))
			{
				b=k;
				break;
			}
		}
		printf("Case #%I64d: %I64d\n",j,b-a+1);
	}
}
