//gonna get that standing ovation
#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t=0;
	
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int smax;
		int count=0;
		int buffer=0;
		string aud;
		cin>>smax;
		cin>>aud;
		
		for(int j=0;j<=smax;j++)
		{
			
			if(aud[j]=='0')
			{
				if(buffer==0)
				{
					
					count++;
				}
				else
				{
					buffer--;
				}	
			}	
			else if((aud[j]-'0')>1)
			{
				
				buffer=buffer+((aud[j]-'0')-1);
			}
		}
		if(count<0)
		{
			count=0;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}	