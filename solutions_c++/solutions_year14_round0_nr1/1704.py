#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cassert>

using namespace std;

int main()
{
	//ifstream fin("test.in");
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	//fout.precision(7);
	int N;
	int row;
	int kill;
	int a, b, c, d; // These are the possible solutions.
	int curr;
	int soln;

	double C, F, X, rate;
	bool done;
	double oldcost, newcost, farmscost;

	fin >> N;
	for (int t = 1; t <= N; t++)
	{
		fout << "Case #" << t << ": ";
		fin >> row;
		for (int i = 1; i <= 4; i++)
		{
			if (i == row)
			{
				fin >> a;
				fin >> b;
				fin >> c;
				fin >> d;
			}
			else
			{
				fin >> kill;
				fin >> kill;
				fin >> kill;
				fin >> kill;
			}
		}
		// Done parsing first grid.

		fin >> row;

		soln = 0;

		for (int i = 1; i <= 4; i++)
		{
			if (i != row)
			{
				fin >> kill;
				fin >> kill;
				fin >> kill;
				fin >> kill;
			}
			else
			{
				for (int j = 1; j <= 4; j++)
				{
					fin >> curr;
					if (curr == a || curr == b || curr == c || curr == d)
					{
						if (soln == 0)
							soln = curr;
						else
							soln = -1; // Bad magician!
					}
				}
			}
		}

		if (soln == 0)
			fout << "Volunteer cheated!" << endl;
		else if (soln == -1)
			fout << "Bad magician!" << endl;
		else
			fout << soln << endl;

	}

	fin.close();
	fout.close();
}


//int main()
//{
//	//ifstream fin("test.in");
//	ifstream fin("A-large-practice.in");
//	ofstream fout("output.txt");
//	int N, C, I;
//	int* values;
//	bool done;
//
//	fin >> N;
//	for (int t = 1; t <= N; t++)
//	{
//		fout << "Case #" << t << ": ";
//		fin >> C;
//		fin >> I;
//		values = new int[I];
//		for (int i = 0; i <= I - 1; i++)
//		{
//			fin >> values[i];
//		}
//		// OK, in theory we have all the values loaded. Now find how to add up to C.
//		done = false;
//		for (int i = 0; i <= I - 1 && !done; i++)
//		{
//			for (int j = i + 1; j <= I - 1 && !done; j++)
//			{
//				if (values[i] + values[j] == C)
//				{
//					fout << i + 1 << " " << j + 1 << endl;
//					done = true;
//				}
//			}
//		}
//		delete [] values; //Haven't tested this but it's needed, right?
//	}
//
//	fin.close();
//	fout.close();
//}