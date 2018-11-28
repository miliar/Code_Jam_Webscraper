#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
#include <cmath>
#include <set>
#define maxl 1000000000
#define mod 1000000007
#define maxn 5010
#define maxs 150
using namespace std;

void solve(){
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double speed = 2;
	double best = x / speed;
	double now  = 0;
	while(true){
		double need = c / speed;
		now += need;
		speed += f;
		double tmp = now + x / speed;
		if(tmp > best) break;
		best = tmp;
	}
	printf("%.10f\n", best);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}

}