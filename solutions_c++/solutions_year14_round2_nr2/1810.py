#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		cout<<"Case #"<<T<<": ";
		int a,b,k;
		cin>>a>>b>>k;
		int count=0;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				if((i&j)<k)
					count++;
		cout<<count<<endl;
	}
}
