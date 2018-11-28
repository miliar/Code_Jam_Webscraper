#include <fstream>

using namespace std;

int main()
{
	int T = 0, answer1 = 0, answer2 = 0;
	int first[4][4] = { };
	int second[4][4] = { };
	ifstream fi("A-small-attempt0.in");
	ofstream fo("Output.txt");
	fi>>T;
	for (int h = 0; h < T; ++h)
	{
		fi>>answer1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fi>>first[i][j];

		fi>>answer2;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				fi>>second[i][j];

		int result = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (first[answer1 - 1][i] == second[answer2 - 1][j])
					if (result == 0) result = first[answer1 - 1][i];
					else result = -1;

		if (result >= 1) fo<<"Case #"<<h + 1<<": "<<result<<endl;
		else if (result == 0) fo<<"Case #"<<h + 1<<": Volunteer cheated!"<<endl;
		else fo<<"Case #"<<h + 1<<": Bad magician!"<<endl;
	}
	fi.close();
	fo.close();
	return 0;
}