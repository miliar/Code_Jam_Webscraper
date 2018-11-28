#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int j=1,t;
//	freopen("A-large.in","rt",stdin);    
//	freopen("output.cpp","wt",stdout);  
    
	cin>>t;
	while(j<=t)
	{
		long long n;
		cin>>n;
		if(!n)
		{
			printf("Case #%d: INSOMNIA\n",j++);
			continue;
		}
		bool visited [10];
		for(int i=0;i<10;i++)
			visited[i]=false;
		long long p=n,i=1;
		while(1)
		{
			p=i*n;
			long long temp=p;
			while(temp)
			{
				visited[temp%10]=true;
				temp=temp/10;
			}

			int flag=1;
			for(int k=0;k<10;k++)
			{
				if(!visited[k])
				{
					flag=0;
					break;
				}
			}
			if(flag)
				break;
			i++;
		}
		printf("Case #%d: %lld\n",j++,p);
	}
}
