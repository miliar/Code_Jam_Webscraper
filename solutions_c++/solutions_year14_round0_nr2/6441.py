#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define long long long
#define f1(i,n) for (int i=1; i<=n; i++)
#define f0(i,n) for (int i=0; i<n; i++)

void minimize(double &a, double b)
	{ if (a>b) a=b; }

double Cost, Delta, Goal;
int t, T;

main(){
	cin >> T;
f1(t,T) {
	cin >> Cost >> Delta >> Goal;
	double Speed=2, Time=0, Min=23e9;
	int Loop=15000000;
	while (Time <= Goal/2+1 && Loop--) {
		minimize(Min, Goal/Speed+Time);
		Time+=Cost/Speed; Speed+=Delta;
//		cout << Time << " " << Speed << " " << Min << endl;
	}
	printf("Case #%d: %.7lf\n", t, Min);
}
}
