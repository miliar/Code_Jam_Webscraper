#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class cookieclickeralpha
{
	private:
		const double BYIELD;

		double fcost, fyield, ctarget;

	public:
		cookieclickeralpha() : BYIELD(2.) {}

		void input() {
			cin >> fcost >> fyield >> ctarget;
		}

		string solve() {
			ostringstream oss;
			double btime = ctarget / BYIELD;
			double fttime = 0.;
			double myield = BYIELD;
			for (int f = 1; ; ++f) {
				fttime += fcost / myield;
				myield += fyield;
				double ntime = fttime + ctarget / myield;
				if (ntime < btime) {
					btime = ntime;
				} else {
					break;
				}
			}
			oss.setf(ios_base::fixed);
			oss.precision(7);
			oss << btime;
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		cookieclickeralpha task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
