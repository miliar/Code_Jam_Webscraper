#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int t = 0;
	fin >> t;
	for (int tt = 0; tt < t; ++tt)
	{
		int smax = 0;
		fin >> smax;
		string s;
		fin >> s;
		int *pNum = new int[smax + 1];
		for (int i = 0; i <= smax; ++i)
			pNum[i] = s[i] - '0';
		
		int curPNum = 0;
		int ans = 0;
		for (int i = 0; i <= smax; ++i)
		{
			int det = i - curPNum;
			
			if(det > 0) 
			{
				ans += det;
				curPNum += det;
			}

			curPNum += pNum[i];
		}

		fout <<"Case #" << (tt + 1) <<": " << ans << endl;

		delete [] pNum;
	}

	return 0;
}