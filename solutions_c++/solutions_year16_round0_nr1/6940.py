#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
int main()
{
	int t=0,m;
	cin>>t;
	m=t;
	while(t--)
	{
		int count=10;
		long long int n,num2,num1,rem,i=1;
		bool visited[11];
		memset(visited,0,sizeof visited);
		scanf("%lld",&n);
			while(1)
			{
			num1=i*n;
			if(count==0)
			{
				printf("Case #%d: %lld\n",m-t,(i-1)*n);
				break;
			}
			if(num1==n && i!=1)
			{
				printf("Case #%d: INSOMNIA\n",m-t);
				break;
			}
			num2=num1;
			while(num2>0)
			{
				rem=num2%10;
				if(visited[rem]==false)
				{
					count--;
					visited[rem]=true;
				}
				num2=num2/10;
			}
			i++;
		}
		}
		return 0;
	}