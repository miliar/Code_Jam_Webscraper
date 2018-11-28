#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(){
	int tc, tcn;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		printf("Case #%d: ", tc+1);
		double best, next, t = 0, dt = 0, r = 2;
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		best = x / r;
		while(1){
			dt = c / r;
			t += dt;
			r += f;
			next = t + x / r;
			if(next > best)
				break;
			best = next;
		}
		printf("%.20lf\n", best);
	}
}
