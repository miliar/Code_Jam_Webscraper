#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int k[t],s[t],c[t];
	for (int i = 0; i < t; i++)
	{
		cin>>k[i]>>c[i]>>s[i];
	}
	for (int i = 0; i < t; i++)
	{
			// cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			// cout<<"Case #"<<i+1<<": "<<an<<endl;
		if (s[i]<k[i]-1)
		{
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
			continue;
		}
		if (k[i]==1)
		{
			cout<<"Case #"<<i+1<<": "<<1<<endl;
			continue;
		}
		if (c[i]==1)
		{
			if (s[i]<k[i])
			{
				cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
				continue;
			}
			cout<<"Case #"<<i+1<<": ";
			for (int j = 1; j <= k[i]; j++)
			{
				cout<<j<<' ';
			}
			cout<<endl;
			continue;
		}
		cout<<"Case #"<<i+1<<": ";
		int p=0;
		for (int j = 2; j <= k[i]; j++,p+=k[i])
			{

				cout<<j+p<<' ';
			}
		cout<<endl;
			continue;
	}
	return 0;
}