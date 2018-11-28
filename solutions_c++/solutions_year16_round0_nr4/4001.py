#include<fstream>
using namespace std;

int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("output.txt");

	int T, K, C, S;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		fin >> K;
		fin >> C;
		fin >> S;

		fout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < K; j++)
		{
			fout << j + 1 << " ";
		}
		fout << endl;
	}

	return 0;
}