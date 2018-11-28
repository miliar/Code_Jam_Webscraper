#include<fstream>
#include<iostream>

using namespace std;

int main()
{
	fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\JAM1out.txt");
	int T,i=1;
	cin>>T;
	while(T)
	{
		long int N;
		cin>>N;
		
		if(N==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			fil<<"Case #"<<i<<": INSOMNIA\n";
		}
		
		else
		{
			int digit[10]={0};
			bool flag=true;
			long int sum=0,tmp;
			while(flag)
			{
				sum+=N;
				tmp=sum;
				int rem;
				while(tmp>0)
				{
					rem=tmp%10;
					digit[rem]=1;
					tmp/=10;	
				}
				int count=0;
				for(int j=0;j<10;j++)
				{
					if(digit[j]==0)
					{
						count++;
						break;
					}
				}
				if(!count)
				flag=false;
			}
				cout<<"Case #"<<i<<": "<<sum<<endl;
				fil<<"Case #"<<i<<": "<<sum<<"\n";	
		}		
		i++;
		T--;
	}
	fil.close();
}
