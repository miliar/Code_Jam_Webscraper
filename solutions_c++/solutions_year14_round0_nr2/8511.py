#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iomanip>

using namespace std;
#define exp 1e-7
#define si 40
#define inf 0x3f
#define INF 0x3f3f3f3f
#define loop(n) for(int i=0;i<n;i++)
#define period(s,e) for(int i=s;i<=e;i++)

int T;
double C, F, X, cookie, rate, pre, current, cc;

double ss(){
	double tmp;
	pre=X/rate;
	cc=C/rate;
	rate+=F;
	current=cc+X/rate;
	while(current<pre){
		pre=current;
		cc+=C/rate;
		rate+=F;
		current=cc+X/rate;
	}
	return pre;
}

int main() {


	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lf%lf%lf",&C,&F,&X);
		rate=2.0;

		printf("Case #%d: %.7lf\n",t, ss());

	}



	return 0;
}