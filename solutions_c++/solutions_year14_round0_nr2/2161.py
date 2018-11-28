#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

long double c, x, f;

void Load()
{
	double cc, ff, xx;
	cin >> cc >> ff >> xx;
	c = cc; f = ff; x = xx;
//	cerr << c << ' ' << f << ' ' << x << '\n';
}

void Solve()
{
	double spent = 0.0;
	double cf = 2.0;
	long long i = 0;
//	cerr << c << ' ' << f << ' ' << x << "\n";
	if (c < x) while (true) {
		if (x * cf < (x - c) * (f + cf)) {
//			cerr << "adding new factory: +";
			i++;     
			spent += c / cf;
//			cerr << c / cf << "\n";
			cf += f;
		} else break;
	}
	spent += x / cf;
	cerr << "got " << i << " factories\n";
//	cerr << "waiting for x: +" << x / cf << "\n";
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(7);
	cout << spent << "\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
