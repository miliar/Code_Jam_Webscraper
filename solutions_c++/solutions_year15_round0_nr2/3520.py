#include <bits/stdc++.h>
#include <iostream>
#include <fstream>

typedef long long ll;
using namespace std;
int main()
{
	ofstream outfile;
	ifstream infile;
	infile.open("B-large.in");
	outfile.open("out2.in");
	int t,i;
	infile>>t;
	for(i=0;i<t;i++)
	{
		int d;
		infile>>d;
		int j;
		std::vector<int> v(d);
		for(j=0;j<d;j++)
		{
			infile>>v[j];
		}
		int ans=10000,x;
		for(x=1;x<=1000;x++)
		{
			int p=0;
			for(j=0;j<d;j++)
			{
				if(v[j]>x)
				{
					p+=v[j]/x;
					if(v[j]%x!=0)
					{
						p++;
					}
					p--;
				}
			}
			ans=min(ans,p+x);
		}
		outfile<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}