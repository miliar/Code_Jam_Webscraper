#include <algorithm>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

// https://mattmccutchen.net/bigint/
#include "bigint-2010.04.30\\BigUnsigned.hh"

using namespace std;

#define IN_FILE "D:\\D-small-attempt0.in"
#define OUT_FILE "D:\\code_jam_out.txt"

void func(ifstream& in, ofstream& out)
{
	int K, C, S;
	in >> K >> C >> S;

	if (S < K - 1 || C == 1 && S < K)
	{
		out << "IMPOSSIBLE" << endl;
		return;
	}

	if (C == 1)
	{
		for (int i = 1; i <= K; i++)
            out << i << " ";
		out << endl;
        return;
	}

	if (K == 1 && S == 1)
	{
        out << "1" << endl;
        return;
	}

	for (int i = 2; i <= K; i++)
		out << i << " ";
    out << endl;
}

int main()
{
	ifstream in;
	in.open(IN_FILE);

	ofstream out;
	out.open (OUT_FILE);
	//out << fixed << showpoint << setprecision(7);

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		//cout << "Case #" << t << endl;
		out << "Case #" << t << ": ";
		//out << "Case #" << t << ":" << endl;
		func(in, out);
	}

	in.close();
	out.close();

	return 0;
}
