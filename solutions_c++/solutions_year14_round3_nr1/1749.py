#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int Q=1;Q<=t;++Q)
	{
		cout<<"Case #"<<Q<<": ";
		long long int p,q;
		char c;
		cin>>p>>c>>q;
		long long int j = 1;
		int i=0;
		while(j<q)
		{
			j*=2;
			i++;
		}
		if(j!=q)
		{
			cout<<"impossible"<<endl;
			continue;
		}
		while(i<40)
		{
			p*=2;
			i++;
		}
		long long int a = 1;
		int k = 0;
		while(a<=p)
		{
			a*=2;
			k++;
		}
		cout<<40-k+1<<endl;
	}
	return 0;
}

