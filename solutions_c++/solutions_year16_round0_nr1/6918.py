#include<bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int T;
	
	cin>>T;
	
	for(int t=1;t<=T;t++)
	{
		long long N;
		int check[10]={0};
		int done = 0;
		
		cin>>N;
		
		if(N==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA\n";
			continue;
		}
		
		int i = 1;
		long long current;
		
		while(1)
		{
			current = N*i;
			
			while(current)
			{
				int r = current%10;
				if(check[r]==0)
				{
					check[r]= 1;
					done++;
				}
				current/=10;
			}
			
			if(done==10)
				break;
			
			i++;
		}
		
		cout<<"Case #"<<t<<": "<<i*N<<"\n";
		
	}
	
	return 0;
}
				 
		
		
		
