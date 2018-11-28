#include <iostream>
using namespace std;

int main() {
	long long t;
	cin>>t;
	for(long long x=1;x<=t;x++)
	{
		long long flag=0;
		long long n=0;
		long long data=0, sol=0;
		long long present[17]={0};
		cin>>n;
		for(long long i=0;i<4;i++)
		{
			for(long long j=0;j<4;j++)
			{
				cin>>data;
				if(i==(n-1))
				{
					present[data]++;
				}
			}
		}
		cin>>n;
		for(long long i=0;i<4;i++)
		{
			for(long long j=0;j<4;j++)
			{
				cin>>data;
				if(i==(n-1))
				{
					present[data]++;
					if(present[data] > 1)
					{
						flag++;
						sol=data;
					}
				}
			}
		}
		cout<<"Case #"<<x<<": ";
		if(flag == 1)
			cout<<sol<<endl;
		else if(flag == 0)
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<"Bad magician!"<<endl;
	}
	return 0;
}
