#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define rep(i,s,e) for (int i=(s);i<(e);++i)
#define pb push_back
#define mk make_pair
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

double r[100];
double c[100];

double eps = 1e-7;

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ": ";
    int n; double v, x;
    cin >> n >> v >> x;
    rep(i,0,n) cin >> r[i] >> c[i];

    double t;
    bool impos = false;
    if (n == 1) {
      if (x != c[0])
        impos = true;
      else
        t = v / r[0];
    } else if (n == 2) {
      if (max(c[0], c[1]) < x || min(c[0], c[1]) > x)
        impos = true;
      else if (c[0] == c[1]) {
        if (c[0] != x) impos = true;
        else t = v / (r[0] + r[1]);
      } else {
        double v0 = (x * v - v * c[1]) / (c[0] - c[1]);
        if (0 <= v0 + eps && v0 - eps <= v)
          t = max(v0 / r[0], (v-v0) / r[1]);
        else
          impos = true;
      }
    }
    if (impos)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << fixed << setprecision(10) << t << endl;
	}
}
