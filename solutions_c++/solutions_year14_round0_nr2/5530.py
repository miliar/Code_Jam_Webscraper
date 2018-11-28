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
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <string.h>
#include <utility>
#include <vector>
using namespace std;
#define exp 1e-9
#define si 40
#define inf 0x3f
#define INF 0x3f3f3f3f
#define loop(n) for(int i=0;i<n;i++)
#define period(s,e) for(int i=s;i<=e;i++)
template<class out_type, class in_value>
out_type convert(const in_value &t) {
	stringstream stream;
	stream << t;
	out_type result;
	stream >> result;
	return result;
}

int sign(double x) {
	return x < -exp ? -1 : x > exp;
}



int T;
double C, F, X, cookie, rate, pre, current, cc;

double solve(){
	double tmp;
	pre=X/rate;
	cc=C/rate;
	rate+=F;
	current=cc+X/rate;
		while((current-pre)<-exp){
		pre=current;
		cc+=C/rate;
		rate+=F;
		current=cc+X/rate;
	}
	return pre;
}

int main() {
#ifndef ONLINE_JUDGE
	//freopen("B-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif

	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lf%lf%lf",&C,&F,&X);
		rate=2.0;

		printf("Case #%d: %.7lf\n",t, solve());

	}



	return 0;
}