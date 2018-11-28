#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin>>t;
	int u = 0;
	while(u++ < t)
	{
		int k;
		fin>>k;
		string str;
		fin>>str;
		int up = 0, extra = 0;
		for (int i = 0; i <= k; ++i)
		{
			int x = (int)(str[i] - '0');
			if(up < i)
			{
				extra += i - up;
				up += i - up;
			}
			up += x;
		}
		fout<<"Case #"<<u<<": "<<extra<<endl;	
	}
	return 0;
}