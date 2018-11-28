//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Problem A. Standing Ovation, Qualification Round 2015
//Czas: Theta(T*S_max)
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define SIZE(x) int((x).size())

int rozwiaz(const string& s)
{
	int wynik = 0, prefiks = 0;
	REP(i, SIZE(s))
	{
		wynik = max(wynik, i - prefiks);
		prefiks += int(s[i]) - int('0');
	}
	return wynik;
}

int zrob_test()
{
	int S_max;
	string s;
	cin >> S_max >> s;
	return rozwiaz(s);
}

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	FOR(i, 1, T)
		cout << "Case #" << i << ": " << zrob_test() << '\n';
	return 0;
}
