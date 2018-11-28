#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int T, cas;
	double p, c, f, x, ans;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		ans = 0;
		p = 2;
		scanf("%lf %lf %lf", &c, &f, &x);
		while (x/p > x/(p+f) + c/p){
			ans += c/p;
			p += f;
		}
		ans += x/p;
		printf("Case #%d: %.7lf\n", cas, ans);
	}
}

