#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cassert>

using namespace std;

int main()
{
	//ifstream fin("test.in");
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	fout.precision(7);
	int N, k;
	double C, F, X, rate;
	bool done;
	double oldcost, newcost, farmscost;

	fin >> N;
	for (int t = 1; t <= N; t++)
	{
		fout << "Case #" << t << ": ";
		fin >> C;
		fin >> F;
		fin >> X;
		oldcost = DBL_MAX;
		farmscost = 0;
		newcost = X / 2.0;
		k = 0;
		
		while (newcost < oldcost)
		{
			oldcost = newcost;
			k++;

			farmscost += C / (2.0 + (k - 1)*F);
			newcost = farmscost + X / (2.0 + k*F);
		}
		// Now oldcost should hold the answer?
		fout << fixed << oldcost << endl;


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