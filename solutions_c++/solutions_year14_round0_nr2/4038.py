#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int t, cases;
double c, f, x, r, ans;

int main() {
	scanf("%d", &t);
	cases = 1;
	while(t--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		
		ans = 0;
		r = 2;
		while ((x/r) > ((c/r) + (x/(r+f)))) {
			ans += c/r;
			r += f;
		}
		ans += x/r;
		printf("Case #%d: %.7lf\n", cases++, ans);
	}
	
	return 0;
}
