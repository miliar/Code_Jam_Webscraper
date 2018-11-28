#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define has(c,i) ((c).find(i) != (c).end())
#define DBG(...) ({ if(1) fprintf(stderr, __VA_ARGS__); })
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int TC;
int N;
double V, X;
double R[2], C[2];
double RR, CC;
double VV;
double S;


double eval(double v1) {
	double v2 = V - v1;
	S = v1 / RR + v2 / R[0];

	double temp = (v1*CC + v2*C[0]) / V;
	return abs(temp - X);
}

double ternary_min(double a, double d) {
  double width = (d - a) * 2;
  FOR(i,0,90) {
    width = d - a;
    double b = a + width / 3;
    double c = a + width * 2 / 3;
    if (eval(b) > eval(c)) a = b;
    else                   d = c;
  }
  return (a + d) / 2.0;
}

int main() {
	ios::sync_with_stdio(false);

	cin >> TC;
	FOR(tc, 1, TC+1) {
		cin >> N >> V >> X;
		FOR(i,0,N) cin >> R[i] >> C[i];

		if (N == 1) {
			if (C[0] == X) {
				printf("Case #%d: %.9lf\n", tc, V / R[0]);
			} else {
				printf("Case #%d: IMPOSSIBLE\n", tc);
			}
			continue;
		}

		if (N == 2) {
			if ((C[0] < X && C[1] < X) || (C[0] > X && C[1] > X)) {
				printf("Case #%d: IMPOSSIBLE\n", tc);
				continue;
			}

			if (C[0] == C[1] && C[0] == X) {
				printf("Case #%d: %.9lf\n", tc, V / (R[0] + R[1]));
				continue;
			}

			CC = (R[0] * C[0] + R[1] * C[1]) / (R[0] + R[1]);
			RR = (R[0] + R[1]);
			if ((CC < X && C[0] < X) || (CC > X && C[0] > X)) {
				swap(R[0], R[1]);
				swap(C[0], C[1]);
			}

			VV = ternary_min(0, V);
			DBGDO(eval(VV));

			printf("Case #%d: %.9lf\n", tc, S);
		} else {
			assert(false);
		}
	}
}
