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

const int MAX = 105;
int R, C, lewy[MAX], prawy[MAX], gora[MAX], dol[MAX];
char t[MAX][MAX];

void wczytaj_dane()
{
	cin >> R >> C;
	REP(i, R)
		REP(j, C)
			cin >> t[i][j];
}

void wypelnij_kierunki()
{
	fill(lewy, lewy + MAX, MAX);
	fill(prawy, prawy + MAX, -1);
	fill(gora, gora + MAX, MAX);
	fill(dol, dol + MAX, -1);
	
	REP(i, R)
		REP(j, C)
			if (t[i][j] != '.')
			{
				lewy[i] = min(lewy[i], j);
				prawy[i] = max(prawy[i], j);
				gora[j] = min(gora[j], i);
				dol[j] = max(dol[j], i);
			}
}

bool jest_ok(int i, int j)
{
	switch (t[i][j])
	{
		case '<':
			return lewy[i] < j;
			break;
		case '>':
			return prawy[i] > j;
			break;
		case '^':
			return gora[j] < i;
			break;
		default:
			return dol[j] > i;
			break;
	}
}

bool mozna_obrocic(int i, int j)
{
	return (lewy[i] < j || prawy[i] > j || gora[j] < i || dol[j] > i);
}

void rozwiaz()
{
	int licz = 0;
	REP(i, R)
		REP(j, C)
			if (t[i][j] != '.' && (! jest_ok(i, j)))
			{
				if (mozna_obrocic(i, j))
					licz++;
				else
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
			}
			cout << licz << '\n';
}

void zrob_test()
{
	wczytaj_dane();
	wypelnij_kierunki();
	rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	FOR(i, 1, T)
	{
		cout << "Case #" << i << ": ";
		zrob_test();
	}
	return 0;
}
