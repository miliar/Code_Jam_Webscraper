#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	string a;
	string b;
	scanf("%d",&T);
	int c=0;
	while(T--)
	{
		b="";
		cin>>a;
		b=b+a[0];
		for(int i=1;i<a.length();i++)
		{
			if(a[i]>=b[0])
			{
				b=a[i]+b;
			}
			else
			{
				b=b+a[i];
			}
		}
		cout<<"Case #"<<++c<<": "<<b<<"\n";
	}
}
