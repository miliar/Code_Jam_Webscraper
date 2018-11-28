#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define FORD(x, a, b) for (int x = (a); x >= (b); x--)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) (int((x).size()))
#define FOREACH(i, c) for (VAR(i, (c).begin()); i != (c).end(); i++)
#define PB push_back
#define ST first
#define ND second
#define POKAZ(x) cerr << #x << " = " << (x) << '\n'

const int MAX = 20, SLOWA = 2010;
int N, slowa;
vector<string> zdanie[MAX];
VI zd[MAX];

void wczytaj_dane()
{
	REP(i, MAX)
		zdanie[i].clear();
	cin >> N;
	string s;
	getline(cin, s);
	REP(i, N)
	{
		stringstream ss;
		getline(cin, s);
		ss << s;
		while (ss >> s)
			zdanie[i].PB(s);
	}
}

void przenumeruj()
{
	REP(i, N)
		zd[i].clear();
	slowa = 0;
	map<string, int> mapa;
	REP(i, N)
		REP(j, SIZE(zdanie[i]))
		{
			if (mapa.find(zdanie[i][j]) == mapa.end())
				mapa[zdanie[i][j]] = slowa++;
			zd[i].PB(mapa[zdanie[i][j]]);
		}
	
	/*REP(i, N)
	{
		REP(j, SIZE(zd[i]))
			cerr << zd[i][j] << ' ';
		cerr << '\n';
	}
	cerr << '\n';*/
}

inline int bit(int m, int i)
{
	return (m >> i) & 1;
}

void jezykuj(int i, int q, bool jezyk[][2])
{
	REP(j, SIZE(zd[i]))
		jezyk[zd[i][j]][q] = true;
}

int rozwaz(int m)
{
	bool jezyk[SLOWA][2];
	REP(i, slowa)
		REP(j, 2)
			jezyk[i][j] = false;
	
	REP(i, N)
		if (i < 2)
			jezykuj(i, i, jezyk);
		else
			jezykuj(i, bit(m, i - 2), jezyk);
	
	int licz = 0;
	REP(i, slowa)
		if (jezyk[i][0] && jezyk[i][1])
			licz++;
	return licz;
}

int rozwiaz()
{
	int wynik = 10001000;
	for (int m = 0; m <= (1 << (MAX - 2)); m++)
		wynik = min(wynik, rozwaz(m));
	return wynik;
}

int zrob_test()
{
	wczytaj_dane();
	przenumeruj();
	return rozwiaz();
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
