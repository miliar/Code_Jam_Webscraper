#include<iostream>
using namespace std;
int T,N;
int sum,E;
char x;
void read()
{

	cin>>T;
	for(int k=1;k<=T;k++)
	{
		sum=E=0;
		cin>>N;
		for(int i=0;i<=N;i++)
		{
			cin>>x;
			if(i>sum && x!='0')
			{
				E+=i-sum;
				sum+=i-sum+x-'0';
			}
			else sum+=x-'0';
		}
		cout<<"Case #"<<k<<": "<<E<<endl;
	}
}
int main()
{
	read();
}
