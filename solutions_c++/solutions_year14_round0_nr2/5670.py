#include <cstdio>
#include <iostream>
using namespace std;

double work() 
{
	double C, F, X, f = 2, tfarm = 0;
	scanf("%lf%lf%lf", &C, &F, &X);
	int farm = 1;
	double ans = tfarm + X / f, newans;
	while(true) {
		tfarm += C / f;
		f += F;
		newans = tfarm + X / f;
		if(newans < ans) {
			ans = newans;
		} else {
			break;
		}
	}
	return ans;
}

int main() 
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++) 
	{
		printf("Case #%d: %.7lf\n", tt, work());
	}
	return 0;
}

