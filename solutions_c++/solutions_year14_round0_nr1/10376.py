#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
	unsigned short T, c1, c2, t1[4][4], t2[4][4];
	ifstream fin("gcj.in");
	fin >> T;
	ofstream fout("gcj.out");
	for (unsigned short i = 1; i <= T; i++)
	{
		fin >> c1;
		c1--;
		for (unsigned short n = 0; n < 4; n++) fin >> t1[n][0] >> t1[n][1] >> t1[n][2] >> t1[n][3];
		sort(t1[c1], t1[c1] + 4);
		fin >> c2;
		c2--;
		for (unsigned short n = 0; n < 4; n++) fin >> t2[n][0] >> t2[n][1] >> t2[n][2] >> t2[n][3];
		sort(t2[c2], t2[c2] + 4);
		unsigned short p1 = 0, p2 = 0, r = 0, h;
		while (p1 < 4 && p2 < 4)
		{
			if (t1[c1][p1] > t2[c2][p2]) p2++;
			else if (t1[c1][p1] < t2[c2][p2]) p1++;
			else
			{
				h = t1[c1][p1];
				r++;
				p1++;
				p2++;
			}
		}
		fout << "Case #" << i << ": ";
		if (r == 1) fout << h << "\n";
		else if (r > 1) fout << "Bad magician!\n";
		else fout << "Volunteer cheated!\n";
	}
	fout.close();
	fin.close();
	return(0);
}