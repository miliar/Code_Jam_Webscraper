//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Problem C. Dijkstra, Qualification Round 2015
//Czas: O(T*(L*X)^2)
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define SIZE(x) int((x).size())
#define POKAZ(x) cerr << #x << " = " << (x) << '\n'

const int MAX = 10100;
int n, t[MAX], pref[MAX];

int numer(char z)
{
	return z == '1' ? 1 : int(z) - int('i') + 2;
}

int znak(int a)
{
	return a > 0 ? 1 : -1;
}

int pomnoz_modul(int a, int b)
{
	if (a == 1)
		return b;
	if (b == 1)
		return a;
	if (a == b)
		return -1;
	return ((a == 3) == (b <= 2 || (a == 2 && b == 3)) ? -1 : 1) * (9 - a - b);
}

int pomnoz(int a, int b)
{
	return znak(a) * znak(b) * pomnoz_modul(abs(a), abs(b));
}

int odwrotnosc(int a)
{
	return abs(a) == 1 ? a : -a;
}

string powtorz(const string& okres, int X)
{
	string s;
	while (X--)
		s += okres;
	return s;
}

void wypelnij_pref()
{
	pref[0] = 1;
	FOR(i, 1, n)
		pref[i] = pomnoz(pref[i - 1], t[i]);
}

int fragment(int a, int b)
{
	return pomnoz(odwrotnosc(pref[a]), pref[b]);
}

bool rozwiaz_naprawde()
{
	wypelnij_pref();
	FOR(i, 1, n)
	{
		if (fragment(0, i) != 2)
			continue;
		FOR(j, i + 1, n)
		{
			if (fragment(i, j) == 3 && fragment(j, n) == 4)
				return true;
		}
	}
	return false;
}

bool rozwiaz(const string& s)
{
	n = SIZE(s);
	REP(i, n)
	{
		t[i + 1] = numer(s[i]);
		//cerr << t[i + 1];
	}
	//cerr << '\n';
	return rozwiaz_naprawde();
}

void zrob_test(int i)
{
	//cerr << '\n';
	//POKAZ(i);
	int L, X;
	string okres;
	cin >> L >> X >> okres;
	cout << "Case #" << i << ": " << (rozwiaz(powtorz(okres, X)) ? "YES" : "NO") << '\n';
}

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	FOR(i, 1, T)
		zrob_test(i);
	return 0;
}
