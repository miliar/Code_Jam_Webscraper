#include <fstream>
using namespace std;

int main()
{
	ifstream in ("2014qualsA.in");
	ofstream out ("2014qualsA.out");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		int num[2], row[2][4];
		for (int i = 0; i < 2; i++)
		{
			in >> num[i];
			num[i]--;
			for (int j = 0; j < 4; j++)
			{
				if (num[i] == j)
					in >> row[i][0] >> row[i][1] >> row[i][2] >> row[i][3];
				else
				{
					int n;
					in >> n >> n >> n >> n;
				}
			}
		}

		int cnt = 0, ans = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (row[0][i] == row[1][j])
				{
					cnt++;
					ans = row[0][i];
				}

		out << "Case #" << t << ": ";
		if (cnt == 1)
			out << ans << "\n";
		else if (cnt == 0)
			out << "Volunteer cheated!\n";
		else
			out << "Bad magician!\n";
	}

	in.close();
	out.close();
	return 0;
}