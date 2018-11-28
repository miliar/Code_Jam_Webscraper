#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
bool palindrome(int n)
{
	if(n<10)
	return true;
	else 
	{
		int m=n;
		int s=0;
		while(m>0)
		{
			s=s*10+(m%10);
			m/=10;
		}
		return s==n;
	}
}
int main()
{
	int t;
	bool test[1001];
	scanf("%d",&t);
	for(int i=0;i<1001;i++)
	test[i]=false;
	for(int i=1;i<=sqrt(1000);i++)
	{
		if(palindrome(i) && palindrome(i*i))
		test[i*i]=true;
	}
	for(int i=1;i<=t;i++)
	{
		int count=0;
		int a,b;
		scanf("%d",&a);
		scanf("%d",&b);
		for(int j=a;j<=b;j++)
		if(test[j])
		count++;
		printf("Case #%d: %d\n",i,count);
	}
}

