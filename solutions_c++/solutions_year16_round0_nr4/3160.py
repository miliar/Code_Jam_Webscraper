#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <math.h>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main(int argc, char const *argv[])
{
	ifstream infile("D-small-attempt2.in");
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	ofstream outfile("D-small-attempt2.out");
	for (int i = 0; i < T; i++)
	{
		int K, C, S;
		infile >> K >> C >> S;
		outfile << "Case #" << i + 1 << ": ";
		for (int j = 0; j < K; j++)
		{
			ull segment = pow(K, C - 1);
			outfile << j * segment + 1 << ' ';
		}
		outfile << endl;
	}
	return 0;
}