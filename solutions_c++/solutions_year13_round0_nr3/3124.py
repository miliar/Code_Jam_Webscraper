#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
bool f(int a)
{
	int s[10];
	int i=0,j;
	while(a>0)
	{
		s[i++]=a%10;
		a/=10;
	}
	for(j=0;j<i;j++)
	{
		if(s[j]!=s[i-1-j])
		{
			return false;			
		}
	}
	return true;
}
bool g(int a)
{
	int b=sqrt(a*1.0);
	if(b*b!=a)
	{
		return false;
	}
	else
	{
		return f(b);
	}
}
int main()
{
	freopen("OUTPUT.txt", "w", stdout);
	int t,a,b,i;
	cin>>t;
	int ca=1,cnt;
	while(t--)
	{
		scanf("%d%d",&a,&b);
		cnt=0;
		for(i=a;i<=b;i++)
		{
			if(f(i)&&g(i))
			{
				cnt++;
			}
		}
		printf("Case #%d: %d\n",ca++,cnt);
	}
	return 0;
}