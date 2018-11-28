#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define INF 1000000000
#define pb push_back 
#define itr iterator 
#define sz size() 
#define mp make_pair

int T, teste;
pair<double, double> src[1100];
int n;
double tgt_v, tgt_x;

bool check(double tm) {
	double V = 0;
	double CV = 0;
	for (int i = n-1; i >= 0; i--) {
		double newV = min(tgt_v - V, src[i].second * tm);
		V += newV;
		CV += (newV/tgt_v) * src[i].first;
	}

	//printf("tm = %f V = %f CV = %f\n", tm, V, CV);

	if (V < tgt_v || CV < tgt_x) return false;

	V = 0;
	CV = 0;
	for (int i = 0; i < n; i++) {
		double newV = min(tgt_v - V, src[i].second * tm);
		V += newV;
		CV += (newV/tgt_v) * src[i].first;
	}

	if (V < tgt_v || CV > tgt_x) return false;

	return true;
}

int main() {
	for (scanf("%d", &T); T; T--) {
		printf("Case #%d: ", ++teste);
		

		scanf("%d %lf %lf", &n, &tgt_v, &tgt_x);
		//printf("targ = %f %f\n", tgt_v, tgt_v * tgt_x);

		double mv = -1;
		for (int i = 0; i < n; i++) {
			double r,c;
			scanf("%lf %lf", &r, &c);
			if (i == 0) mv = r;
			else mv = min(mv, r);
			src[i] = mp(c,r);
		}

		sort(src, src+n);
		bool ok = false;

		double st = 0, ed = tgt_v / mv + 1e-9;
		for (int it = 0; it < 1000; it++) {
			double mid = (st+ed)/2;
			if (check(mid)) {
				ed = mid;
				ok = true;
			}
			else st = mid;
		}

		if (!ok) printf("IMPOSSIBLE\n");
		else printf("%.15f\n", ed);
	} 
}