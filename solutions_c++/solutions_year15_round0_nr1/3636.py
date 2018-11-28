#include <bits/stdc++.h>
#include <iostream>
#include <fstream>

typedef long long ll;
using namespace std;
int main()
{
	ofstream outfile;
	ifstream infile;
	infile.open("A-large.in");
	outfile.open("outA.in");
	int t;
	infile>>t;
	int i;
	for(i=0;i<t;i++)
	{
		int smax;
		infile>>smax;
		string x;
		infile>>x;
		std::vector<int> v(smax+1);
		int j;
		for(j=0;j<smax+1;j++)
		{
			v[j] = x[j]-'0';
		}
		int y = v[0],ans=0;
		for(j=1;j<smax+1;j++)
		{
			if(j<=y)
			{
				y+=v[j];
			}
			else
			{
				ans+=(j-y);
				y = j+v[j];
			}
		}
		outfile<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}