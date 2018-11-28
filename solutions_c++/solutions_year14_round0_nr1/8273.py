#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int T;
	ifstream in ("A.in");
	ofstream out("A.out");
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		int row1;
		in >> row1;
		int game1[4][4];
		row1--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> game1[i][j];
			}
		}
		int row2;
		in >> row2;
		row2--;
		int game2[4][4];
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> game2[i][j];
			}
		}
		vector<int> ans;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (game1[row1][i] == game2[row2][j])
					ans.push_back(game1[row1][i]);
			}
		}
		out << "Case #" << t << ": ";
		if (ans.size() == 0)
			out << "Volunteer cheated!" << endl;
		else if (ans.size() == 1)
			out << ans[0] << endl;
		else
			out << "Bad magician!" << endl;
	}	
	return 0;
}
