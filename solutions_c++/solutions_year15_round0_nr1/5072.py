#include <iostream>
#include <cstdio>
using namespace std;
void process()
{
	int n,t=0,r=0;
	cin>>n;
	char x;
	for(int i=0;i<n+1;i++)
	{
		scanf(" %c",&x);
		x-='0';
		//cout<<(int)x<<endl;
		if(t>=i){
			t+=x;
		}
		else
		{
			r+=i-t;
			t+=i-t+x;
		}
		//cout<<"T"<<t<<endl;
	}
	cout<<r<<endl;
	//cout<<"BITTI"<<endl;
}
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{	cout<<"Case #"<<i+1<<": ";
		process();
	}
}