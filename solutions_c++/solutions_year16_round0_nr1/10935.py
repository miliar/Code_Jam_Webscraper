#include<iostream>
#include<cstdio>
using namespace std;
bool flag[10];
bool f()
{
	for(int i=0;i<10;++i)
	{
		if(flag[i]==false)
			return false;
	}
	return true;
}
void fi(int num)
{
	int a=num;
	while(a!=0)
	{
		flag[a%10]=true;
		a/=10;
	}
}
int main()
{
	int T;
	int n;
	cin>>T;
	int i,j,k;
	for(k=0;k<T;++k)
	{
		cin>>n;
		for(i=0;i<10;++i)
		{
			flag[i]=false;
		}
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",k+1);
		}
		else
		{
			int sum=n;
			while(!f())
			{
				fi(sum);
				sum+=n;
			}
			printf("Case #%d: %d\n",k+1,sum-n);
		}
	}
	return 0;
}