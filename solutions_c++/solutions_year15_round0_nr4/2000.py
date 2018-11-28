//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Problem D. Ominous Omino, Qualification Round 2015
//Czas: Theta(T*S_max)
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)

bool rozwiaz(int x, int r, int c)
{
	switch (x)
	{
		case 1:
			return true;
		case 2:
			return (r * c) % 2 == 0;
		case 3:
			return (r >= 2 && c >= 3) && (r * c) % 3 == 0;
		case 4:
			return r >= 3 && c >= 4;
	}
	assert(false);
}

int zrob_test()
{
	int x, r, c;
	cin >> x >> r >> c;
	return rozwiaz(x, min(r, c), max(r, c));
}

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	FOR(i, 1, T)
		cout << "Case #" << i << ": " << (zrob_test() ? "GABRIEL" : "RICHARD") << '\n';
	return 0;
}
