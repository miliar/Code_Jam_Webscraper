#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#define VAR(i,v) auto i = (v)
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define REP(i,b) for(int i=0; i<(b); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;
typedef vector<int> VI;
typedef long long LL;

const double MAXN = 100002;
int n;


int main() {
	cin >> n;

	REP(i,n) {
		double c, f, x;
		cin >> c >> f >> x;

		double prod = 2;
		double tot_time = 0;
		double prev = MAXN;


		while(true) {
			double tm = (x / prod) + tot_time;
			//cout << "tm = " << tm << ", prod = " << prod << ", tot_time = " << tot_time << endl;
			tot_time += (c / prod);
			prod += f;
			if (tm > prev) break;
			prev = tm;
		}

		cout << fixed << setprecision(9) << "Case #" << i+1 << ": " << prev  << endl;
	}

	return 0;
}
