#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	cout << fixed;
	for(int t = 1; t <= T; ++t) {
		long double C, F, X, cookies = 0, cps = 2;
		long double ans = 0;

		cin >> C >> F >> X;
		
		while(cookies < X) {
			long double t1 = X / cps;
			long double t0 = C / cps;
			long double t2 = t0 + X / (cps + F);
		
			if(t1 < t2) {
				ans += t1;
				break;
			} else {
				ans += t0;
				cps += F;
			}
			
		}
		
		cout << "Case #" << t << ": " <<ans << endl;
	}
}
