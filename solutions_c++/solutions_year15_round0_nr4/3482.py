#include <string>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("output.txt");
	if(fin.is_open())
	{
		int t; fin>>t;
		for (int i = 1; i <= t; ++i)
		{
			int x,r,c; string res;
			fin>>x>>r>>c;
			if(x<7)
			{
				if((r%x==0 && c>=x-1) || (c%x==0 && r>=x-1))
					res = "GABRIEL";
				else
					res = "RICHARD";
			}
			else
				res = "RICHARD";
			fout<<"Case #"<<i<<": "<<res<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}