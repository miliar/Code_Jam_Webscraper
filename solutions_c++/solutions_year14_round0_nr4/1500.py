#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cassert>
#include <algorithm>

using namespace std;
//
//int main()
//{
//	//ifstream fin("test.in");
//	ifstream fin("A-small-attempt0.in");
//	ofstream fout("output.txt");
//	//fout.precision(7);
//	int N;
//	int row;
//	int kill;
//	int a, b, c, d; // These are the possible solutions.
//	int curr;
//	int soln;
//
//	double C, F, X, rate;
//	bool done;
//	double oldcost, newcost, farmscost;
//
//	fin >> N;
//	for (int t = 1; t <= N; t++)
//	{
//		fout << "Case #" << t << ": ";
//		fin >> row;
//		for (int i = 1; i <= 4; i++)
//		{
//			if (i == row)
//			{
//				fin >> a;
//				fin >> b;
//				fin >> c;
//				fin >> d;
//			}
//			else
//			{
//				fin >> kill;
//				fin >> kill;
//				fin >> kill;
//				fin >> kill;
//			}
//		}
//		// Done parsing first grid.
//
//		fin >> row;
//
//		soln = 0;
//
//		for (int i = 1; i <= 4; i++)
//		{
//			if (i != row)
//			{
//				fin >> kill;
//				fin >> kill;
//				fin >> kill;
//				fin >> kill;
//			}
//			else
//			{
//				for (int j = 1; j <= 4; j++)
//				{
//					fin >> curr;
//					if (curr == a || curr == b || curr == c || curr == d)
//					{
//						if (soln == 0)
//							soln = curr;
//						else
//							soln = -1; // Bad magician!
//					}
//				}
//			}
//		}
//
//		if (soln == 0)
//			fout << "Volunteer cheated!" << endl;
//		else if (soln == -1)
//			fout << "Bad magician!" << endl;
//		else
//			fout << soln << endl;
//
//	}
//
//	fin.close();
//	fout.close();
//}


int main()
{
	//ifstream fin("test.in");
	ifstream fin("D-large.in");
	ofstream fout("output.txt");
	int N, numwts;
	double *valuesA, *valuesB;
	//bool done;

	int place;
	int score;

	fin >> N;
	for (int t = 1; t <= N; t++)
	{
		fout << "Case #" << t << ": ";
		fin >> numwts;
		valuesA = new double[numwts];
		for (int i = 0; i <= numwts - 1; i++)
		{
			fin >> valuesA[i];
		}
		valuesB = new double[numwts];
		for (int i = 0; i <= numwts - 1; i++)
		{
			fin >> valuesB[i];
		}
		// OK, in theory we have all the values loaded.

		// First need to sort our lists.
		
		sort(valuesA, valuesA + numwts);
		sort(valuesB, valuesB + numwts);
		
		//////////for (int i = 0; i <= numwts - 1; i++)
		//////////	cout << valuesA[i] << " ";
		//////////cout << endl;
		//////////for (int i = 0; i <= numwts - 1; i++)
		//////////	cout << valuesB[i] << " ";
		//////////cout << endl;
		
		// Now let's play the game.

		// First play with cheating.

		place = numwts - 1;
		score = 0;

		for (int i = numwts - 1; i >= 0; i--)
		{
			if (valuesB[i] < valuesA[place])
			{
				place--;
				score++;
			}
		}
		fout << score << " ";

		// Now play without cheating.

		place = numwts - 1;
		score = 0;

		for (int i = numwts - 1; i >= 0; i--)
		{
			if (valuesA[i] < valuesB[place])
			{
				place--;
				score++;
			}
		}
		fout << numwts - score << endl;


		delete [] valuesA;
		delete[] valuesB;
	}

	fin.close();
	fout.close();
}