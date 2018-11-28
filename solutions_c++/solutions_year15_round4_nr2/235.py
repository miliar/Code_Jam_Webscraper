#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<iostream>
#include <iomanip> 

// macros

#define FORE(c, a, b) for(int c=a; c<= int(b); ++c)
#define FORD(c, a, b) for(int c=a; c>= int(b); --c)
#define FORIT(it, cont, cont_t) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define ALL(a) a.begin(), a.end() 
#define PR(n) printf("%d ", (int) (n)) 
#define PRL(n) printf("%lld ", (ll) (n)) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0)
#define prd dbg printf

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<double, double> pd;
typedef vector<pd> vdi;
typedef vector<vi> vvi;

// actual code

const int NMAX = 200;
const double MINTEMP = 0.0, MAXTEMP = 100000.0;

int tt, n;
double xx, vv, r[NMAX], c[NMAX], mini, maxi;

void solve(int ti) {
	cin >> n >> vv >> xx;
	mini = MAXTEMP, maxi = MINTEMP;
	double out = 0.0, upsum = 0.0, upmass = 0.0, downsum = 0.0, downmass = 0.0;
	
	REP(i, n) {
		cin >> r[i] >> c[i];
		mini = min(mini, c[i]);
		maxi = max(maxi, c[i]);
		if(c[i] > xx) {
			upsum += r[i] * (c[i] - xx);
			upmass += r[i];
		}
		else {
			downsum += r[i] * (xx - c[i]);
			downmass += r[i];
		}
	}
	if (xx < mini || xx > maxi) {
		cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
		return;
	}
	//prd("%lf %lf %lf %lf\n", upsum, upmass, downsum, downmass);
	dbg cout << upsum << " " << upmass << " " << downsum << " " << downmass << endl;
	
	vdi krany;
	if (upsum < downsum) {
		out += upmass;
		REP(i, n) if(c[i] <= xx)
			krany.pb(mp(xx - c[i], r[i]));
		sort(ALL(krany));
		
		REP(i, krany.size()) {
			double dx = krany[i].xx, rr = krany[i].yy;
			if(upsum >= rr * dx) {
				out += rr;
				upsum -= rr * dx;
			}
			else {
				out += upsum / dx;
				break;
			}
		}	
	} else {
		out += downmass;
		REP(i, n) if(c[i] > xx)
			krany.pb(mp(c[i] - xx, r[i]));
		sort(ALL(krany));
		
		REP(i, krany.size()) {
			double dx = krany[i].xx, rr = krany[i].yy;
			if(downsum >= rr * dx) {
				out += rr;
				downsum -= rr * dx;
			}
			else {
				out += downsum / dx;
				break;
			}
		}	
	}
	dbg cout << out << endl;
	cout << "Case #" << ti << ": " << std::setprecision(15) << (vv / out) << endl;
}

int main() {
	cin >> tt;
	REP(ti, tt)
		solve(ti + 1);
	return 0;
}
