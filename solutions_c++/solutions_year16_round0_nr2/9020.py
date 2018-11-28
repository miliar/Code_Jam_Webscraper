#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		string a;
		cin>>a;
		long long int x=0;
		for(int i=1;i<a.length();i++)
		{
			if(a[i]=='-'&&a[i-1]=='+')
				x++;
		}
		cout<<"Case #"<<j<<": ";
		if(a[0]=='-')
			cout<<2*x+1<<endl;
		else cout<<2*x<<endl;
	}
}