#include <bits/stdc++.h>
using namespace std;
int a[2000];
int main()
{
	int test;
	cin>>test;
	for(int z=1;z<=test;z++)
	{
		int n;
		cin>>n;
		string s;
		cin>>s;
		for(int i=0;i<=n;i++)
		{
			a[i]=s[i]-'0';
		}
		int x;
		for(x=0;;x++)
		{
			int p = x;
			bool psbl = 1;
			for(int i=0;i<=n;i++)
			{
				if(p<i)
				{
					psbl=0;break;
				}
				p+=a[i];
			}
			if(psbl)break;
		}
		cout<<"Case #"<<z<<": "<<x<<endl;
	}
}
