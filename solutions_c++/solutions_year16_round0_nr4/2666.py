#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			int k, c, s; in >> k >> c >> s;
			out << "Case #" << t << ":";
			if (s != k) out << " IMPOSSIBLE";
			else for (int i = 1; i <= k; ++i) out << " " << i;
			out << '\n';
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
