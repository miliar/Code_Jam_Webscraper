#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("data.txt");
	ofstream fout("ans.txt");
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		int m;
		char in[1010] = {};
		fin >> m >> in;
		int re = 0;
		int need = 0;
		for(int j = 0; j <= m; j++)
		{
			if(need < j && in[j] > '0') 
			{
				re += (j - need);
				need = j;
			}
			need += in[j] - '0';
			
		}
		fout << "Case #" << (i + 1) << ": " << re << endl;
	}
	return 0;
}
