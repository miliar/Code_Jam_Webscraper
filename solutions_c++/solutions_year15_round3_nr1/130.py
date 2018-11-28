#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

ifstream in("aa2.in");
ofstream out("aa2.out");

int main()
{
	int test;
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		int answer = 0, R, C, W;
		in >> R >> C >> W;
		if (W == 1)
			answer = R * C;
		else
		{
			if (C % W == 0)
				answer = R * (C / W) + W - 1;
			else
				answer = R * (C / W) + W;

		}
		out << "Case #" << t << ": " << answer << endl;
	}
}