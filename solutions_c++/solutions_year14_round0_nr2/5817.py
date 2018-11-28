#include <iostream>
using namespace std;



int main() {
	
	int T;
	cin >> T;

	for (int ts=1; ts<=T; ++ts) {
		double C, F, X;
		cin >> C >> F >> X;
		double rate = 2.0;
		double ans = X / rate;
		double tm = 0.0;
		for (int i=1; i<=200000; ++i) {
			tm += C / rate;
			rate += F;
			double cur_ans = tm + X / rate;
			if (cur_ans < ans)
				ans = cur_ans;
		}
		cout.setf(ios::fixed);
		cout.precision(8);
		cout.setf(ios::showpoint);
		cout << "Case #" << ts << ": " << ans << endl;
	}



	return 0;
}
