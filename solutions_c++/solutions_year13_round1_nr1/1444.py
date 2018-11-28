#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<math.h>
#include<algorithm>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	for(int i=1;i<=T;++i)
	{
		long long int r,t;
		fin>>r>>t;
		long long int paintR = 0;
		long long int count = 0;
		while(paintR <= t)
		{
			paintR += 2*r + 1;
			r +=2;
			++count;
		}
		--count;
		fout<<"Case #"<<i<<": "<<count<<endl;
	}
	fout.close();
	fin.close();
}
