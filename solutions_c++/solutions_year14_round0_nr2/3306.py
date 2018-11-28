#include <bits/stdc++.h>
using namespace std;
int ntc;
double c, f, x, r, t, ans;
int main(){
	scanf("%i", &ntc);
	for(int tc=1;tc<=ntc;tc++){
		r = 2;
		t = 0;
		scanf("%lf %lf %lf", &c, &f, &x);
		ans = x / r;
		while(1){
			t += c / r;
			r += f;
			if(t + x/r > ans) break;
			ans = min(ans, t + x / r);
		}
		printf("Case #%i: %.7lf\n", tc, ans);
	}
}