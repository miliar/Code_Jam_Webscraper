#include <iostream>
#include <cstdio> 
#include <algorithm>
#include <vector>
#include <cstring>
#define maxn 105
#define inf 0x3fffffff
#define exp 1e-8
using namespace std;

double c, f, x;

int isbuy(double v, double c, double f, double x){
	double t1 = x / v;
	double t2 = c / v + x / (f + v);
	if (t1 < t2) return 0;
	else return 1;
}

int main(){
	freopen("B-large.in","r",stdin); 
	freopen("out.txt","w",stdout); 
	int T;
	cin >> T;
	int cas = 1;
	while (T--){
		scanf("%lf%lf%lf", &c, &f, &x);
		double t = 0.0;
		double cookies = 0.0;
		double v = 2.0;
		while (isbuy(v, c, f, x)){
			t += c / v;
			v += f;
		}
		t += x / v;
		
		printf("Case #%d: %.7f\n", cas++, t);
	}
	return 0;
}