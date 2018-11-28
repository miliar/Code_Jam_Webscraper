using namespace std;
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using uint = unsigned long long;

vector< vector< int > > v;
vector< uint > divs;
char s[50];

bool ok();
uint get_div(uint);
uint get_num(int);

int main()
{
	int i, n, j, t, tests;
	bool gata;
	ifstream fin("data.in");
	ofstream fout("data.out");

	fin >> tests >> n >> j;
	s[1] = s[n] = '1'; s[n + 1] = '\0';
	for (i = 2; i < n; ++i) s[i] = '0';

	fout << "Case #1:\n";
	for (t = 1, gata = 0; !gata && t <= j; )
	{
		if (ok())
		{
			fout << s + 1;

			for (auto &div : divs)
				fout << ' ' << div;
			fout << '\n';

			++t;
		}

		for (i = n - 1; i > 1 && s[i] == '1'; --i) s[i] = '0';
		if (i == 1) gata = true;
		else s[i] = '1';
	}

	fin.close();
	fout.close();

    return 0;
}

bool ok()
{
	divs.clear();

	for (int base = 2; base <= 10; ++base)
	{
		uint x = get_num(base);
		uint div = get_div(x);

		if (div == 0) return false;
		divs.push_back(div);
	}

	return true;
}

uint get_div(uint x)
{
	// we know that x is odd

	for (int d = 3; d * d <= x; d += 2)
		if (x % d == 0) return d;

	return 0;
}

uint get_num(int base)
{
	int i;
	uint res;

	for (res = 0, i = 1; s[i]; ++i)
		res = res * base + s[i] - '0';

	return res;
}