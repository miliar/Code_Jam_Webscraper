#include<iostream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output7.in","w",stdout);
	long int t;
	cin>>t;
	long int k = t;
	while(t--)
	{
		long long int n;
		cin>>n;
		
		int count = 10;
		int map[10];
		
		for(int i=0;i<10;i++)
		{
			map[i] = 0;
		}
	
		
		if(n==0)
		{
			cout<<"CASE #"<<k-t<<": INSOMNIA\n";
		}
		else
		{
			long int loopCount = 1;
			
			while(count>0)
			{
				long long int num = loopCount * n;
				
				while(num>0)
				{
					int rem = num%10;
					
					if(map[rem]==0)
					{
						map[rem] = 1;
						count -- ;
					} 
					
					num = num / 10;
				}				
				
				loopCount ++;
			}
			cout<<"CASE #"<<k-t<<": "<<(loopCount-1)*n<<"\n";
		}
		
	}
}
