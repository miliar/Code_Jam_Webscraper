#include<stdio.h>
#include<iostream>
#include<map>

using namespace std;

int ans[2000000];

int main()
{
	int i, ct;
	
	for(i = 1; i <= 1200000; i++)
	{
		ct = 0;
		
		map<int, int> mp;
		int x = 0;
		
		int j = 0;
		
		while(ct != 10)
		{
			j++;
			x = x + i;
			
			int y = x;
			
			while(y != 0)
			{
				if(mp[y%10] == 0)
				{
					mp[y%10] = 1;
					ct++;	
				}	
				
				y = y/10;
			}	
			
		}
		
		ans[i] = x;		
	}
	
	int t;
	
	cin>>t;
	
	int rt = 0;
	
	while(t--)
	{
		rt++;
		cin>>i;
		
		if(ans[i] != 0)
		cout<<"Case #"<<rt<<": "<<ans[i]<<"\n";
		
		else
		{
		cout<<"Case #"<<rt<<": "<<"INSOMNIA"<<"\n";
		}
	}
	
	return 0;
}
