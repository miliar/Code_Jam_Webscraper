#include <string>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	if(fin.is_open())
	{
		int t; fin>>t;
		for (int i = 1; i <= t; ++i)
		{
			int smax,count=0,res=0; string s;
			fin>>smax; fin>>s;
			for (int j = 0; j <= smax; ++j)
			{
				if(count<j && s[j]!='0')
				{
					res += (j-count);
					count += res;
				}
				count+=(s[j]-'0');
			}
			fout<<"Case #"<<i<<": "<<res<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}