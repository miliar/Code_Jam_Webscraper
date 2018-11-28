#include <cstdio>
#include <cmath>

using namespace std;

	int t;
	double c,f,x,l,time,r;

int main() {

	freopen ("B-large.in","r",stdin);
	freopen ("Output.in","w",stdout);
	scanf("%d",&t);
	for (int k=1; k<=t; k++) {
		scanf("%lf %lf %lf",&c,&f,&x);
		r = 2;
		time = 0;
		l = f*(x/c - 1);
		if (l <= 2) printf("Case #%d: %.7lf\n",k,(double)x/2);
		else {
			l -= 2;
			l = ceil(l/f);
			while (l-- > 0) {
				time += c/r;
				r += f;
			}
			time += x/r;
			printf("Case #%d: %.7lf\n",k,time);
		}
	}

	return 0;
}
