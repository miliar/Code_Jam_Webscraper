#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

void solve(int nT){
	long double ans, initC;
	long double C,F,X;
	cin >> C >> F >> X;
	ans = X / 2.0;
	initC = 0;
	long double cur = 2;
	for (int i=1; true; i++){
		initC += (long double)C / (long double)cur;
		cur += F;
		long double tmp = initC+(long double)X/(long double)cur;
		ans = min(ans,tmp);
		if (tmp > ans && i >= 3000000)
			break;
	}
	printf("Case #%d: %.7f\n", nT, (double)ans);
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int i=1; i<=nT; i++)
		solve(i);
	return 0;
}