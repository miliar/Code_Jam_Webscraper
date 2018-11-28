#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in ("A-small-attempt0.in");
	ofstream out ("ans.txt");
	int t;
	in >> t;
	for (int iter = 0; iter < t; iter++)
	{
		int g1, g2, x[4][4], y[4][4], count = 0, num = 0;
		in >> g1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				in >> x[i][j];
		in >> g2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				in >> y[i][j];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (x[g1-1][i] == y[g2-1][j])
				{
					count++;
					num = x[g1-1][i];
				}
		out << "Case #" << iter+1 << ": ";
		if (count == 0)
			out << "Volunteer cheated!";
		else if (count == 1)
			out << num;
		else if (count > 1)
			out << "Bad magician!";
		out << endl;
	}
	return 0;
}
