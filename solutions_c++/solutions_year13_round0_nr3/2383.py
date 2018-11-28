#include<iostream>
#include<stdio.h>
using namespace std;

long long int a[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
	int test,times,i,key1,key2;
	long long int m,n;
	scanf("%d",&times);
	for(test=1;test<=times;test++)
	{
		scanf("%lld %lld",&m,&n);
		for(i=0;i<39;i++)
			if(a[i]>=m)
				break;
		key1=i;
		for(i=38;i>=0;i--)
			if(a[i]<=n)
				break;
		key2=i;
		if(key2-key1<0)
			printf("Case #%d: 0\n",test);
		else
			printf("Case #%d: %d\n",test,key2-key1+1);
	}
	return 0;
}

