#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for (int x = b; x <= (e); x++)
#define FORD(x, b, e) for (int x = b; x >= (e); x--)
#define REP(x, n) for (int x = 0; x < (n); x++)

const int INF = 1000000000;
const double PI = acos(-1);
const double EPS = 10e-9;

int main()
{
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	REP(i,t)
	{
		double r, zapas;
		cin >> r >> zapas;
		double wynik;
		int licznik = 0;
		double suma = 0;
		r += 1.0;
		while (suma <= zapas)
		{
			wynik = r * r - ((r-1.0)*(r-1.0));
			licznik++;
			if (suma + (wynik) <= zapas)
				suma += wynik;
			else
				break;
			r = r + 2.0; 
		}
		cout << "Case #" << i + 1 << ": " << licznik - 1 << endl;
	}

	system("pause");
	return 0;
}
