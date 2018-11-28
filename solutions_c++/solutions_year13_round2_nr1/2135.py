#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#define SIZE 128
using namespace std;
int a[SIZE];
int need(int a,int b,int & c);
int main()
{
	int cas,n;
	int c,t;
	cin>>cas;
	for(int q = 1;q<=cas ;q++)
	{
		int sol = 0;
		cin>>c>>n;
		for(int i = 0 ;i < n ; i++)
			cin>>a[i];
		sort(a,a+n);
		
		for(int i = 0 ;i < n ; i++)
		{
			int num = need(c,a[i],t);
			if(num >= ( n-i))
			{
				sol+=(n-i);break;
			}
			else
			{
				c = t + a[i];
				sol+=num;
			}
		}
		printf("Case #%d: %d\n",q,sol);
	}
	return 0;
}
int need(int a,int b,int & c)
{
	if(a== 1)return 1e7;
	int cnt = 0;
	while(a <= b)
	{
		a+=(a-1);
		cnt++;
	}
	c = a;
	return cnt;
}
