#include<bits/stdc++.h>
using namespace std;
#define d(x) cout<<#x<<" is "<<x<<endl;
int main()
{
	long long int t;
	cin>>t;
	for(long long int t1=1;t1<=t;t1++)
	{
		long long int n;
		cin>>n;
		long long int t=n;
		bool num[10];
		for(long long int i=0;i<10;i++)
		{
			num[i]=false;
		}
		if(n==0)
		{
			cout<<"Case #"<<t1<<": INSOMNIA"<<endl;
		}
		else
		{
			long long int c=1;
			while(1)
			{
				//d(t);
				long long int count=0;
				t=c*n;
				long long int z=t;
				while(z>0)
				{
					num[z%10]=true;
					z=z/10;
				}
				
				for(long long int i=0;i<10;i++)
				{
					if(num[i]==true)
					{
					//cout<<" "<<i;
					count++;
					}
					
				}
				//cout<<endl;
				if(count==10)
				{
					break;
				}
				c++;
				
			}
			cout<<"Case #"<<t1<<": "<<t<<endl;
		}
	
	}
}
