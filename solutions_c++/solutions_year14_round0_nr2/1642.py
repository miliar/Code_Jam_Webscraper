#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		double C, F, X;
		cin >> C >> F >> X;
		double ans = 0;
		double v = 2;
		while(X > 0) {
			if(X > C) {
				ans += C / v;
				if(((X-C) / v) > (X / (v + F))) {
					v += F;
				} else {
					X -= C;
				}
			} else {
				ans += X / v;
				X = 0;
			}

		}
		printf("Case #%d: %.7f\n", i+1, ans);
	}
	return 0;
}