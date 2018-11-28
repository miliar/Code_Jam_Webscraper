#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++ i) {
		double C, F, X, curr = 0, ans = 0;
		int farms = 0;
		cin >> C >> F >> X;
		while(curr < X) {
			if(curr < C) {
				if(C < X) {
					ans += (C - curr) / (2 + F * farms);
					curr = C;
				}
				else {
					ans += (X - curr) / (2 + F * farms);
					curr = X;
				}
			}
			else {
				double left = (X - curr) / (2 + F * farms);
				double farm = curr - C + left * (2 + F * (farms + 1));
				if(farm > X) {
					++ farms;
					curr -= C;
				}
				else {
					ans += left;
					curr = X;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << ans << endl;
	}
}