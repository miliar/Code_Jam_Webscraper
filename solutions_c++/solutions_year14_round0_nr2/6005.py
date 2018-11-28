#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
using namespace std;

const double eps = 1e-8;

void conduct() {
	double a, b, t, cur, mst, ans;
	scanf("%lf%lf%lf", &b, &t, &a);
	mst=(a-b)/b*t;
	for (ans=0.0, cur=2.0; cur-mst<-eps; cur+=t) ans+=b/cur;
	ans+=a/cur;
	printf("%.7f\n", ans);
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
