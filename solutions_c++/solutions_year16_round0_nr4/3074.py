#include <stdio.h>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

__int64 Pow(__int64 b, __int64 p)
{
	if (p == 0)
		return __int64(1);
	else if (p == 1)
		return b;
	else {
		__int64 result = b;
		while (p > 1)
		{
			p--;
			result *= b;
		}
		return result;
	}
}

string Compute(int K, int C, int S)
{
	bool possible = K - C + 1 <= S;
	if (!possible)
		return " IMPOSSIBLE";

	// Compute tiles that must be uncovered by ensuring that each tile from initial set of K is
	// covered by a combination

	stringstream result;
	__int64 col = 0;

	int cc = C - 1;

	for (int i = 0; i < K; i++)
	{
		col += __int64(i) * Pow(K, cc);

		if (cc == 0 || i == K - 1)
		{
			result << " " << (col + __int64(1));
			cc = C - 1;
			col = 0;
		}
		else
			cc--;
	}

	return result.str();
}

int main(int argc, char** argv)
{
	fstream fin;

	fin.open("D-small-attempt0.in", std::ios::in);

	if (!fin.is_open())
		return -1;

	fstream fout;
	fout.open("D-small-attempt0.out", std::ios::out);

	if (!fout.is_open())
		return -1;

	int T;

	fin >> T;

	for (int i = 0; i < T; i++)
	{
		int K = 0;
		int C = 0;
		int S = 0;

		fin >> K >> C >> S;

		fout << "Case #" << (i + 1) << ":" << Compute(K, C, S) << std::endl;
	}

	fin.close();
	fout.close();

	return 0;
}
