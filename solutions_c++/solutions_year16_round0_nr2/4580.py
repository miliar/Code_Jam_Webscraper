//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Revenge of the Pancakes, Qualification Round 2016
//Czas: Theta(T*|S|)
#include <bits/stdc++.h>
using namespace std;

#define REP(x, n) for (int x = 0; x < (n); x++)
#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define SIZE(x) int((x).size())

string S;
int n;

void wczytaj_dane()
{
	cin >> S;
	n = SIZE(S);
}

int rozwiaz()
{
	int licz = 1;
	FOR(i, 1, n - 1)
		if (S[i] != S[i - 1])
			licz++;
	return licz - (S[n - 1] == '+' ? 1 : 0);
}

int zrob_test()
{
	wczytaj_dane();
	return rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	FOR(t, 1, T)
		cout << "Case #" << t << ": " << zrob_test() << '\n';
	return 0;
}
