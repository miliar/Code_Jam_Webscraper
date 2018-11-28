#include<iostream>
#include<string>
#include<fstream>
using namespace std;
ifstream fin("inp.txt");
ofstream fout("out.txt");

int main()
{
	int T;
	fin >> T;
	for (int bn = 1; bn <= T; bn++)
	{
		long long A, B, K;
		long long nr = 0;
		fin >> A >> B >> K;
		for (int i = 0; i < A; i++)
			for (int j = 0; j < B; j++)
			{
				int a = i&j;
				if (a < K)
				{
					nr++;
				}
			}
		fout <<"Case #"<<bn<<": "<<nr << endl;
	}
	return 0;
}