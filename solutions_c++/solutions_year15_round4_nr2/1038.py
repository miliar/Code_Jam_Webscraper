#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <array>
#include <climits>
#include <bitset>
#include <cassert>


#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define UNIQUE(v) (v).erase(unique(ALL(v)), (v).end())
#define MP make_pair
#define MT make_tuple

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;
typedef long double ld;

ld vx[110], vc[110];
ld V, X;
int n;

const ld EPS = 1e-9;

ld f(ld xy, ld y, ld ab, ld b){
	return (xy - ab) / (y - b);
}

bool func(ld t){
	vector<pair<ld, ld>> v(n);
	ld vsum = 0, tsum = 0;
	rep(i, n){
		v[i] = MP(vc[i], vx[i] * t);
		vsum += vx[i] * t;
		tsum += vx[i] * t * vc[i];
	}

	if (tsum/vsum > X){
		sort(REV(v));
		rep(i, n){
			ld lb = 0, ub = v[i].second;
			rep(j, 200){
				ld mid = (lb + ub) / 2;
				ld newx = f(tsum, vsum, mid*v[i].first, mid);
				if (newx < X + EPS) ub = mid;
				else lb = mid;
			}
			tsum -= ub*v[i].first, vsum -= ub;
			if (abs(tsum / vsum - X) < EPS) break;
		}
	}
	else if (tsum/vsum < X){
		sort(ALL(v));
		rep(i, n){
			ld lb = 0, ub = v[i].second;
			rep(j, 200){
				ld mid = (lb + ub) / 2;
				ld newx = f(tsum, vsum, mid*v[i].first, mid);
				if (newx > X - EPS) ub = mid;
				else lb = mid;
			}
			tsum -= ub*v[i].first, vsum -= ub;
			if (abs(tsum / vsum - X) < EPS) break;
		}
	}
	return vsum > V;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);

	int T;
	cin >> T;
	for (int CASE = 1; CASE <= T; ++CASE){
		cin >> n >> V >> X;
		rep(i, n) cin >> vx[i] >> vc[i];

		ld lb = 0, ub = 1.5e8;
		rep(i, 200){
			ld mid = (lb + ub) / 2;
			if (func(mid)) ub = mid;
			else lb = mid;
		}

		cout << "Case #" << CASE << ": ";

		if (n == 1){
			if (abs(vc[0] - X) < EPS){
				cout << V / vx[0] << endl;
			}
			else{
				cout << "IMPOSSIBLE" << endl;
			}
		}
		else if (n == 2){
			if (vc[0] > vc[1]){
				swap(vc[0], vc[1]);
				swap(vx[0], vx[1]);
			}
			if (vc[0] <= X && X <= vc[1]){
				if (vc[0] == vc[1]) vx[0] += vx[1];
				if (vc[0] == X) cout << V / vx[0] << endl;
				else if (vc[1] == X) cout << V / vx[1] << endl;
				else{
					ld x = (X - vc[0]) / (vc[1] - X);
					ld y = vx[0] * x <= vx[1] ? vx[0] * (1 + x) : vx[1] * (1 + 1 / x);
					cout << V / y << endl;
				}
			}
			else{
				cout << "IMPOSSIBLE" << endl;
			}
		}

		continue;
		if (ub > 1.1e8) cout << "IMPOSSIBLE" << endl;
		else cout << ub << endl;
	}

}