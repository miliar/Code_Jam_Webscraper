#include <fstream>
#include <iostream>
#include <string>
using namespace std;

bool happyCookies[100];
int  N;
int countFlips = 0;

inline void flip(int n)
{
	if (n == 0)
		return;
	for (int i = 0; i < n; ++i)
		happyCookies[i] = !happyCookies[i];
	++countFlips;
}

void solve()
{
	for (;;)
	{
		int pos = 0;
		bool top = happyCookies[0];
		while (pos < N && top == happyCookies[pos])
		{
			++pos;
		}
		if (pos == N) {
			if (!top) 
				++countFlips;
			return;
		}
		flip(pos);
	}
}

int main()
{
	fstream inFile("B-Large.in", ios::in);
	fstream outFile("B-Large.out", ios::out);
	int tests;
	inFile >> tests;
	for (int i = 0; i < tests; ++i)
	{
		string line;
		inFile >> line;
		N = line.size();
		for (int i = 0; i < N; ++i) {
			happyCookies[i] = (line[i] == '+');
		}
		countFlips = 0;
		solve();

		outFile << "Case #" << (i + 1) << ": " << countFlips << endl;;

	}
	return 0;
}

