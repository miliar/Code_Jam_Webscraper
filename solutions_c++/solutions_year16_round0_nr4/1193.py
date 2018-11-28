#include<iostream>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		int k,c,s;
		cin>>k>>c>>s;
		for(int i=0;i<s;i++)
		cout<<i+1<<" ";
		cout<<endl;
	}
}
