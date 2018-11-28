#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double  C, F, X;
int T;
int cas = 0;

int main() {
    freopen("b.in" , "r", stdin);
    freopen("b.out", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		scanf("%lf%lf%lf", &C, &F, &X);
        double ans = 1234567890.0;
		int flag = 1;
		int n = 0;
		while(flag) {
			flag = 0;
			double v = 2;
			double t = 0;
			for(int i = 0; i < n; i++) {
				t += C / v;
				v += F;
			}
			t += X / v;
			if(t < ans) ans = t, flag = 1;
			n++;
		}
		printf("Case #%d: ", ++cas);
		printf("%.7lf\n", ans);
	}
}
