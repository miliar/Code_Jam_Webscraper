#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <functional>
#include <cmath>
#include <string>
#include <queue>
#include <numeric>
#include <map>
#include <set>

using namespace std;


int main(int argc, char *argv)
{
	ifstream ifs("A-small-attempt0.in");
	ofstream ofs("A-small-attempt0.out");
	unsigned int nb_cases;
	ifs >> nb_cases;
	for (unsigned int i = 0; i < nb_cases; i++)
	{
		ofs << "Case #"<<i+1<<": ";
		// do for each case
		int arrangement1[4][4];
		int ch1;
		ifs >> ch1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				ifs >> arrangement1[j][k];
		int arrangement2[4][4];
		int ch2;
		ifs >> ch2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				ifs >> arrangement2[j][k];
		int match_cnt = 0;
		int match_label;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (arrangement1[ch1-1][j] == arrangement2[ch2-1][k])
				{
					match_cnt++;
					match_label = arrangement1[ch1-1][j];
				}
			}
		}
		if (match_cnt == 1)
			ofs << match_label;
		else if (match_cnt == 0)
			ofs << "Volunteer cheated!";
		else
			ofs << "Bad magician!";
		ofs << endl;
	}
	return 0;
}