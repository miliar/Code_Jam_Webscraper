#include <fstream>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");

int main ()
{
	int T;
	int N;
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		int H[3000] = {0};
		fin >> N;
		for (int i = 0; i < 2 * N - 1; i++)
			for (int j = 0; j < N; j++)
			{
				int a;
				fin >> a;
				H[a]++;
			}
		fout << "Case #" << t << ":";
		for (int i = 1; i <= 2800; i++)
			if (H[i] % 2 == 1)
				fout << " " << i;
		fout << endl; 
	}
}

