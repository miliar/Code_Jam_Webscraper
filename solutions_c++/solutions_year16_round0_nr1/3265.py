#include <iostream>
#include <fstream>
#include <unordered_set>

using namespace std;

using ull = unsigned long long;

void retrieve(unordered_set<int>& seen, ull n)
{
	ull tmp = n;
	while (tmp > 0)
	{
		ull last = tmp % 10;
		if (seen.find(last) == seen.end()) seen.insert(last);
		tmp /= 10;
	}
}

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			ull n; in >> n;
			unordered_set<int> seen;
			retrieve(seen, n);
			ull index = 2;
			ull m = n * index;

			while (seen.size() < 10 && m != n)
			{
				retrieve(seen, m);
				++index;
				m = n * index;
			}
			out << "Case #" << t << ": ";
			if (seen.size() == 10) out << (n * (index - 1)) << "\n";
			else out << "INSOMNIA\n";
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
