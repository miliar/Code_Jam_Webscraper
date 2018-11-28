//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2015
//Strona: https://code.google.com/codejam/
//Zadanie: Counting Sheep, Qualification Round 2016
//Czas: Theta(T*log(N))
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)

int N;
bool jest[10];

void dodaj_cyfry(int n)
{
	while (n > 0)
	{
		jest[n % 10] = true;
		n /= 10;
	}
}

bool wszystkie_cyfry()
{
	REP(i, 10)
		if (! jest[i])
			return false;
	return true;
}

int rozwiaz()
{
	fill(jest, jest + 10, false);
	int n = N;
	while (true)
	{
		dodaj_cyfry(n);
		if (wszystkie_cyfry())
			return n;
		n += N;
	}
}

int zrob_test()
{
	cin >> N;
	if (N == 0)
		return -1;
	return rozwiaz();
}

int main()
{
	int T;
	cin >> T;
	FOR(t, 1, T)
	{
		cout << "Case #" << t << ": ";
		int wynik = zrob_test();
		if (wynik ==  -1)
			cout << "INSOMNIA\n";
		else
			cout << wynik << '\n';
	}
	return 0;
}
