#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <iostream>
using namespace std;
#define maxn 10000010
double d[maxn];

void work() {
	double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	d[0] = 0.0;
	for (int i=1 ; i<maxn ; i++ ) {
		double v = (i-1)*f + 2.0;
		d[i] = d[i-1] + c/v;
	}
	double ans = x/2.0;
	for (int i=0 ; i<maxn ; i++ ) {
		double need = d[i] + x/(2.0+i*f);
		ans = min(ans,need);
	}
	printf("%.7lf\n",ans);
}

int main() {
	int cas;
	freopen("test.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	scanf("%d",&cas);
	for (int t=1 ; t<=cas ; t++ ) {
		printf("Case #%d: ",t);
		work();
	}
	return 0;
}