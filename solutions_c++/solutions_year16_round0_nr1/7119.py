#include <bits/stdc++.h>
using namespace std;

int solve(int n)
{
	vector<int> a(10);
	int count = 0, i=1, tmp = n;
	while(1)
	{
		while(n)
		{
			int t = n%10;
			if(a[t] == 0)
			{
				count++;
				a[t] = 1;
			}
			n/=10;
		}
		if(count == 10)
		{
			return i;
		}
		i++;
		n = i*tmp;
	}
}

int main()
{
	int t,n[101],i=0;
	cin>>t;
	while(i++<t)
	{
		cin>>n[i];
	}
	i=0;
	while(i++<t)
	{
		cout<<"Case #"<<i<<": ";
		if(n[i] == 0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{
			cout<<solve(n[i])*n[i]<<endl;
		}
	}
}