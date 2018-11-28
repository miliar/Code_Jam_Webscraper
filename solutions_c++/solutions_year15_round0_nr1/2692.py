#include <fstream>
using namespace std;

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");


	int T;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		int smax;
		char s[2000];
		fin >> smax;
		fin >> s;

		int skipz = 0;
		int result = 0;
		for (int i = 0; i < smax; i++)
		{
			if (s[i] != '0')
			{
				skipz += s[i] - '1';
			}
			else {
				if (skipz > 0)
					skipz--;
				else
					result++;
			}
		}

		fout << "Case #" << (t + 1) << ": " << result << endl;
	}
}