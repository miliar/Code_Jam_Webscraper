#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
long long int solve(int K, int C, int S)
{
	return 0;
}
int main()
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");

	//	ofstream fout1("in.txt");
	//	fout1 << 1000000 << endl;
	//	for (int i = 0; i < 1000000; i++)
	//		fout1 << i << endl;
	int test_cases;
	fin >> test_cases;
	int num123 = 1;
	while (test_cases--)
	{
		char s[200];
		string a;
		long long int  result,K,C,S;
		fin >> K >>C>>S;
//		result = solve(K,C,S);
		if (S >= K){
			fout << "Case #" << num123 << ": ";
			long long int pow12 = 1;
			for (int i = 0; i < C; i++)
				pow12 = pow12*K;
			if (K != 1)
				pow12 = (pow12 - 1) / (K - 1);
			else
				pow12 = 0;
			
			for (int i = 0; i < S; i++)
				fout << i*pow12 + 1 << " ";

			fout << endl;
		}
		else
		{
			fout << "Case #" << num123 << ": " << "IMPOSSIBLE" << endl;
		}
		num123++;
	}
	return 0;
}