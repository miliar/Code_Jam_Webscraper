#include <fstream>

using namespace std;

int main ()
{
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	int CaseCount;
	fin >> CaseCount;
	for (int CaseNum = 1; CaseNum <= CaseCount; CaseNum++)
	{
		int N;
		fin >> N;
		if (N != 0)
		{
			int Multiplyer = 0;
			int NumTracker[10] = {0}, NumTrackerCount = 0;
			while (NumTrackerCount < 10)
			{
				Multiplyer += N;
				int k = Multiplyer;
				while (k > 0)
				{
					NumTracker[k % 10] = 1;
					k /= 10;
				}
				NumTrackerCount = 0;
				for (int i = 0; i <= 9; i++)
					NumTrackerCount += NumTracker[i];
			}
			fout << "Case #" << CaseNum << ": " << Multiplyer << endl;
		}
		else
			fout << "Case #" << CaseNum << ": INSOMNIA" << endl;
	}
	return 0;
}

