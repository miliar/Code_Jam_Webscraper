#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(){
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t){
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double prod = 2.0, dt = x / prod, tacum = 0.0;
		double next = (c / prod) + (x / (prod + f));
		while (dt > next){
			tacum += c / prod;
			prod += f;
			dt = x / prod;
			next = (c / prod) + (x / (prod + f));
		}

		tacum += dt;
		printf("Case #%d: %lf\n", t, tacum);
	}
	return 0;
}
