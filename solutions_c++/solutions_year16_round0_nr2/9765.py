#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

void solve()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		char pancakes[256];
		in >> pancakes;

		int op = 0;
		char prev = '+';
		int len = strlen(pancakes);
		for (int i = 0; i < len; i++)
		{
			if (prev != pancakes[i])
			{
				if (prev == '+')
					op += (i == 0 ? 1 : 2);
				prev = pancakes[i];
			}
		}

		out << "Case #" << t << ": " << op << endl;
	}
}


int main(int argc, char** argv)
{
	solve();
	return 0;
}