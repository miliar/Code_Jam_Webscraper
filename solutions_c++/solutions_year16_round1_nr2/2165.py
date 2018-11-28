#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;
#define maxn 51

int main()
{
	int ncases, N;
	int tmp;
	int check[maxn*maxn];

	ifstream in;
	ofstream out;
	in.open("B/B-large.in");
	out.open("B/B-large-results.out");
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		out << "Case #" << t << ":";
		memset(check, 0, sizeof(int)*maxn*maxn);

		in >> N;

		for (int i = 0; i < 2 * N*N - N; i++)
		{
			in >> tmp;
			check[tmp]++;
		}

		for (int i = 0; i < maxn*maxn; i++)
		{
			if (check[i] % 2 != 0)
			{
				out << " " << i;
			}
		}

		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}