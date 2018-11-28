#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef unsigned int uint;

int lottery(uint A, uint B, uint K)
{
	int res = 0;
	uint tmp;
	for (uint i = 0; i < A; ++i)
	{
		for (uint j = 0; j < B; ++j)
		{
			tmp = i&j;
			if (tmp < K)
				++res;
		}
	}
	return res;
}

int main(int argc, char* argv[])
{
	ifstream in("B-small-attempt0.in");
	ofstream out("result.txt");
	int T, A, B, K;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> A >> B >> K;
		out << "Case #" << i+1 << ": " << lottery(A,B,K) << endl;
	}

	in.close();
	out.close();
	return 0;
}