#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <fstream>
using namespace std;
typedef long long ll;
bool used[10];
bool f()
{
	for (int i=0;i<10;i++)
		if (used[i]==false)
			return false;
	return true;
}
int main()
{
	//ifstream cin("A-large.in");
	//ofstream cout("A-large.out");
	int t,n;
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		cin>>n;
		if (n==0)
		{
			cout<<"Case #"<<cas<<": INSOMNIA\n";
			continue;
		}
		memset(used,false,sizeof(used));
		int k=1;
		while (f()==false)
		{
			ll temp=1LL*n*k;
			while (temp)
			{
				used[temp%10]=true;
				temp/=10;
			}
			k++;
		}
		ll ans=1LL*n*(k-1);
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}