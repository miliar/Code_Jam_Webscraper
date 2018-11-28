//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2017
//Strona: https://code.google.com/codejam/
//Zadanie: Oversized Pancake Flipper (Large), Qualification Round 2017
//Czas: Theta(T*|S|*K)
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define SIZE(x) int((x).size())

const char SUMA = char('-' + '+');
int n, K;
string S;

void wczytaj_dane()
{
	cin >> S >> K;
	n = SIZE(S);
}

void obroc(int i)
{
	assert(i + K <= n);
	REP(j, K)
		S[i + j] = char(SUMA - S[i + j]);
}

bool wszystkie_szczesliwe()
{
	REP(i, n)
		if (S[i] == '-')
			return false;
	return true;
}

int rozwiaz()
{
	int licz = 0;
	FOR(i, 0, n - K)
		if (S[i] == '-')
		{
			obroc(i);
			licz++;
		}
	return wszystkie_szczesliwe() ? licz : -1;
}

int zrob_test()
{
	wczytaj_dane();
	return rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(t, 1, T)
	{
		cout << "Case #" << t << ": ";
		int wynik = zrob_test();
		if (wynik == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << wynik << '\n';
	}
	return 0;
}
