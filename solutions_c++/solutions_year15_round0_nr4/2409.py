#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ifstream fin("input.in");
	ofstream fout("output.txt");
	
	ll t;
	fin>>t;
	ll c=0;
	while(t--)
	{
		c++;
		fout<<"Case #"<<c<<": ";
		ll x,r,c;
		fin>>x>>r>>c;
		if((r*c)%x==0)
		{
			if((r*c)/x >=x-1)
			{
				fout<<"GABRIEL"<<endl;
			}
			else
			{
				fout<<"RICHARD"<<endl;
			}
		}
		else
		{
			fout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
