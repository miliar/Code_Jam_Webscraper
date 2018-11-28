#include <cstdio>
#include <cstring>
#include <iostream>
#define EPS 1e-8
using namespace std ;
double c, f, x, mid, rt, lt;
bool F(double t) {
	double cur = 0 , rate = 2 , money = 0 , target = (c < x ? c : x) ;
    for (;;) {
		if (cur >= t) return false ;
		if (money >= x) return true ;
		if (cur + (x - money) / rate <= t) return true ;
		if (money < target) { double dt = (target - money) / rate ; money = target ; cur += dt ; }
		else if (cur + c / f < t) { money -= c ; rate += f ; }
		else                { double dt = (x      - money) / rate ; money = x      ; cur += dt ; }
	}
}
int main() {
//	freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out","w",stdout) ;
	freopen("B-large.in", "r", stdin); freopen("B-large.out","w",stdout) ;
    int Test ; scanf("%d" , &Test) ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        scanf("%lf %lf %lf" , &c , &f , &x) ;
		printf("Case #%d: " , i) ;
        for ( lt = 0 , rt = x * 0.5 ; (rt - lt) > EPS ; ) {
            mid = (rt + lt) * 0.5 ;
            if (F(mid)) rt = mid ; else lt = mid ;
        }
        printf("%.7lf\n", mid);
	}
}
