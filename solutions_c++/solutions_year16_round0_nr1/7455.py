#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		
		long long n,as[10]={0},count=0,h,ans;
		int inc=1;
		cin>>n;
		h=n;
		if(n==0)
		{
			cout<<"Case #" <<i<<": "<<"INSOMNIA"<<endl;
			
		}
		else{
			while(1)
			{
			
				while(n>0)
				{
					as[n%10]=1;
					n=n/10;
				}
				count=0;
				for(int j=0;j<10;j++)
				{	
					//cout<<as[j]<<endl;
					if(as[j]==1)
						count++;
				}
				if(count==10)
				{
					cout<<"Case #" <<i<<": "<<h*inc<<endl;
					
					break;
				}
				inc++;
				n=h*inc;
			
			
			}
		}
	
	}


	return 0;
}
