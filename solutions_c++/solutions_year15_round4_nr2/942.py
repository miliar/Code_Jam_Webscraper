
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const int MAX = 2;
const double EPS = 1E-8;

bool almost(double a, double b) {
	return abs(a - b) < EPS;
}

struct Input {
	int N;
	double Vt, Tt;
	double V[MAX];
	double T[MAX];

};

struct Output {
	bool possible = true;
	double value;
};

Output compute(Input in) {
	Output out;

	if (in.N == 1) {
		if (almost(in.T[0], in.Tt)) {
			out.value = in.Vt / in.V[0];
		} else {
			out.possible = false;
		}
	} else {
		// N == 2!!!
		if (almost(in.T[0], in.T[1])) {
			if (almost(in.Tt, in.T[0])) {
				out.value = in.Vt / (in.V[0] + in.V[1]);
			} else {
				out.possible = false;
			}
		} else {
			long double v0 = (in.Vt * in.Tt - in.Vt * in.T[1]) / (in.T[0] - in.T[1]);
			long double v1 = in.Vt - v0;
			if (v0 < -EPS || v1 < -EPS) {
				out.possible = false;
			} else {
				long double t0 = v0 / in.V[0];
				long double t1 = v1 / in.V[1];
				//cout << "DEBUG: v0 = " << v0 << ", v1 = " << v1 << ", t0 = " << t0 << ", t1 = " << t1 << endl;
				out.value = (t0 > t1) ? t0 : t1;
			}
		}
	}

	return out;
}

ostream & operator << (ostream & out, const Output & output) {
	if (output.possible) {
		return (out << setprecision(10) << output.value);
	} else {
		return (out << "IMPOSSIBLE");
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		Input in;
		cin >> in.N;
		cin >> in.Vt;
		cin >> in.Tt;
		for (int i = 0; i < in.N; i++) {
			cin >> in.V[i];
			cin >> in.T[i];
		}

		Output out = compute(in);
		cout << "Case #" << t << ": " << out << endl;
	}

	return 0;
}
