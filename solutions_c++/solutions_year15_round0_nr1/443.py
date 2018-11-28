#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int main ()
{
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		int L;
		fin >> L;
		int s = 0, ans = 0;
		for (int i = 0; i <= L; i++)
		{
			char c;
			fin >> c;
			if (s < i)
			{
				ans += (i - s);
				s = i;
			}
			s += (c - '0');
		}
		fout << "Case #" << t << ": " << ans << endl;
	}
}
