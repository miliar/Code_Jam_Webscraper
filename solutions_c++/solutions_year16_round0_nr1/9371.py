#include<iostream>
#include<cstring>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("A-large-output.txt");
	long long t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long long n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<":"<<" INSOMNIA"<<endl;
		}
		else
		{
			long long m=n,start=1,k=n;
			long long a[15]={0};
			while(1)
			{
				long long count=0;
				for(int j=0;j<10;j++)
				{
					if(a[j]!=0)
					{
						count++;
					}
				}
				if(count==10)
				{
					cout<<"Case #"<<i<<": "<<m-k<<endl;
					break;
				}
				else
				{
					while(n>0)
					{
						long long temp=n%10;
						a[temp]++;
						n=n/10;
					}
				}
				start++;
				m=k*start;
				n=m;
			}
		}
	}
}
