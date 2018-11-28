#include<stdio.h>
#include<math.h>

int cod(long long int a);
int checkpal(long long int a);

int main()
{
	int t=1,T;
	scanf("%d",&T);
	while(t<=T)
	{
		long long int A, B;
		//int Ad,Bd,ad,bd;
		scanf("%lld %lld",&A,&B);
		/*Ad=cod(A);
		Bd=cod(B);
		ad=Ad/2;
		bd=Bd/2+1;*/
		long long int low=(sqrtl(A)-(int)sqrtl(A))==0?sqrtl(A):sqrtl(A)+1, high=sqrtl(B);
		long long int i;
		int count=0;
		//printf("low:%lld high:%lld\n",low,high);
		for(i=low; i<=high; i++)
		{
			//if(i*i<A || i*i>high)
				//continue;
			if(checkpal(i))
				continue;
			if(checkpal(i*i))
				continue;
			//printf("checkpal(%lld):%d checkpal(%lld):%d\n",i,checkpal(i),i*i,checkpal(i*i));
			count++;
		}
		printf("Case #%d: %d\n",t,count);
		t++;
	}
}

int cod(long long int a)
{
	int count=0;
	while(a!=0)
	{
		count++;
		a/=10;
	}
	return count;
}

int checkpal(long long int a)
{
	long long int b=0,temp=a;
	while(temp!=0)
	{
		b*=10;
		b+=temp%10;
		temp/=10;
	}
	return a==b?0:1;
}