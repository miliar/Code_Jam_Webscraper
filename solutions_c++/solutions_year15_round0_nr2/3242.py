#include <iostream>
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
		int D;
		int max_P = 0;
		int P[1010] = {};
		fin >> D;
		for(int j = 0; j < D; j++)
		{
			fin >> P[j];
			if(P[j] > max_P) max_P = P[j];
		}
		
		int ans = max_P;
		for(int j = 1; j < max_P; j++)
		{
			int aaa = j;
			for(int k = 0; k < D; k++)
			if(P[k] % j == 0) aaa += P[k] / j - 1;
			else aaa += P[k] / j;
			if(aaa < ans) ans = aaa;
		}
		
		fout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
