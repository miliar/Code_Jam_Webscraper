//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Fractiles, Qualification Round 2016
//Czas: Theta(T*(C+S))
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
#define FOR(x, a, b) for (LL x = (a); x <= (b); x++)
#define REP(x, n) for (LL x = 0; x < (n); x++)

LL K, C, S;

void wczytaj_dane()
{
	cin >> K >> C >> S;
}

void zrob_test()
{
	wczytaj_dane();
	LL pot = 1;
	REP(q, C - 1)
		pot *= K;
	REP(i, S)
		cout << 1 + i * pot << ' ';
	cout << '\n';
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	LL T;
	cin >> T;
	FOR(t, 1, T)
	{
		cout << "Case #" << t << ": ";
		zrob_test();
	}
	return 0;
}
