#include <bits/stdc++.h>

using namespace std;

int t, m;
char x;

ifstream in("ovation.in");
ofstream out("ovation.out");

int main ()
{
	in >> t;
	for (int i = 0; i < t; ++i) {
		int a = 0, b = 0;
		in >> m;
		for (int j = 0; j <= m; ++j) {
			in >> x, x -= '0';
			b = max(b, j - a);
			a += x;
		}
		out << "Case #" << i + 1 << ": " << b << '\n';
	}
}

