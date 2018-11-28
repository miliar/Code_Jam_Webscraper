#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    double C, F, X;
	cin >> C >> F >> X;
	double best = X / 2.0;
	double accm = 0;
	for (int i = 1; ; ++i) {
		accm += C / (2 + F * (i - 1));
		double t = accm + X / (2 + F * i);
		if (t > best) break;
		best = t;
	}
	cout << "Case #" << cn << ": ";
  	cout << setprecision(10) << fixed << best << endl;
  }
  return 0;
}
