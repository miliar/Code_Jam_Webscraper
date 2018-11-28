#include<cstdio>
#include<iostream>
#include<map>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	
	int cnt = 1;
	while(t--)
	{
		long long n;
		scanf("%lld", &n);
		
		if(n == 0)
		{
			cout<<"Case #"<<cnt<<": INSOMNIA"<<endl;
			cnt++;
			continue;
		}
		
		bool seen[10];
		map<long long, bool> visited;
		
		long long i;
		for(i=0;i<10;i++)
			seen[i] = false;
		
		for(i=1;i<=100;i++)
		{
			long long cn = i*n;
			while(cn!=0)
			{
				seen[cn%10] = true;
				cn/=10;
				
			}
			
			bool fd = true;
			long long j;
			for(j=0;j<10;j++)	
			{
				fd = fd&&seen[j];
			}
			if(fd)
				break;
				
		}
		cout<<"Case #"<<cnt<<": "<<(i*n)<<endl;
		cnt++;
		
		
	}
	
	
	
}