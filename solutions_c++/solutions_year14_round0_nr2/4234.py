#include<fstream>
#include<iomanip>

using namespace std;

double production, past, wait, buy, remained, ret;
double c, f, x;
int t;

int main() {

	ifstream cin("B-large.in", fstream::in);
	ofstream cout("out.out", fstream::out);

	if (!cin) return 1;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> c >> f >> x;
		production = 2.0;
		past = 0;
		wait = x / production;
		buy = x / (production + f) + c / production;

		while (buy < wait) {
			past += c / production;
			production += f;
			wait = x / production;
			buy = x / (production + f) + c / production;
		}

		ret = past + wait;
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << ret << endl;
	}

	return 0;
}