#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

using ll = long long;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			string data; in >> data;
			ll cnt = 0;
			ll p = 0;
			ll m = 0;
			while (p < data.size())
			{
				p = 0;
				m = 0;
				while (m < data.size() && data[m] != '+') ++m;
				while (p < data.size() && data[p] != '-') ++p;
				if (p < data.size())
				{
					int l = 0;
					int r = max(m, p) - 1;
					while (l < r)
					{
						swap(data[l], data[r]);
						data[l] = (data[l] == '-') ? '+' : '-';
						data[r] = (data[r] == '-') ? '+' : '-';
						++l;
						--r;
					}
					if (l == r) data[l] = (data[l] == '-') ? '+' : '-';
					++cnt;
				}
			}
			out << "Case #" << t << ": " << cnt << '\n';
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
