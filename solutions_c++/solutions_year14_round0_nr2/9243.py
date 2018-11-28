#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; --a)
#define MOD 1000000000
#define MODLL 1000007LL
#define INF 2123123123
#define pb push_back
using namespace std;

int main() {
	int T;
	double c, f, x;
	
	scanf("%d", &T);
	
	FORU(tc, 1, T) {
		printf("Case #%d: ", tc);
		
		scanf("%lf %lf %lf", &c, &f, &x);
		
		double cps = 2.0;
		double cookie = 0;
		double ans = 0;
		
		while (cookie < x) {
			double time1 = x / cps;
			double time2 = (c / cps) + (x / (cps + f));
			
			if (time1 <= time2) {
				cookie = x;
				ans += time1;
			}
			else {
				ans += c / cps;
				cps += f;
			}
		}
		
		printf("%.7lf\n", ans);
	}
}
