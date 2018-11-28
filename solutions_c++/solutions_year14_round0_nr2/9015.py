#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		double C, F, X; cin >> C >> F >> X;
		double ans = X / 2;
		double fm = 0;
		for (int i = 0; ; i++) {
			fm += C / (2 + i*F);
			double new_score = fm + X / (2 + (i+1) * F);
			if (new_score > ans) {
				
				break;
			} else {
				ans = new_score;
			}
		}
		printf("Case #%d: %.7f\n", No, ans);
	}
	return 0;
}
