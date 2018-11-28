#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <iomanip>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;


int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		long double c, f, x;
		long double inc = 2.;
		cin >> c >> f >> x;
		double ct = 0;
		while((x / inc + ct) > (x / (inc + f) + ct + c / inc)) {
			ct += c / inc;
			inc += f;
		}
		long double res = ct + x / inc;
		cout << fixed << setprecision(8) << "Case #" << t << ": " << res  << endl;

	}
	return 0;
}
