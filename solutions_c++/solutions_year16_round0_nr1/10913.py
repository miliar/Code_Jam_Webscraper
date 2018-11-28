#include <fstream>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	int T, N, caseN = 1;
	long k, j;
	fin >> T;
	while (T--)
	{
		set<int> S;
		fin >> N;
		int i = 1;

		if (N == 0)
		{
			fout << "Case #" << caseN << ": " << "INSOMNIA" << endl;
			caseN++;
			continue;
		}

		while (S.size() != 10)
		{
			k = j = N * i;
			while (k > 0)
			{
				S.insert(k % 10);
				k /= 10;
			}
			i++;
		}

		fout << "Case #" << caseN << ": " << j << endl;

		caseN++;
	}
	fin.close();
	fout.close();
	return 0;
}