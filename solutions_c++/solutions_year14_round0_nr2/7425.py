#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

const int maxn=205;

double c,f,x;

void solve() {
	double ans=0;
	double now=2.0;
	while (true) {
		double t=c/now;
		double t2=x/now;
		if (t+x/(now+f)<t2) {
			ans+=t;
			now+=f;
		}
		else break;
	}
	ans+=x/now;
	printf("%.7lf\n",ans);
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>c>>f>>x;
		cout<<"Case #"<<++kase<<": ";
		solve();
	}
	return 0;
}
