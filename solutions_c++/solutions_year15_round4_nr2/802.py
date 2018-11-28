#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

#define EPS 1e-10

using namespace std;

/*bool is_possible(double t, const vector<double>& R, const vector<double>& C, vector<bool>& ex, double V, double X, int N) {
	if ((X < 0) || (V < 0)) {
		return false;
	}

	double total_rate_b = 0.0;
	double total_rate_a = 0.0;

	double total_temp_a = 0.0;
	double total_temp_b = 0.0;
	
	for (int i = 0; i < N; ++i) {
		if (!ex[i]) {
			if (X > C[i]) {
				total_rate_b += R[i];
				total_temp_b += R[i]*C[i];
			} else {
				total_rate_a += R[i];
				total_temp_a += R[i]*C[i];
			}
		}
	}

	double t_b = 

	if (total_vol < V) {
		return false;
	}

	if ((total_vol_b > V) && (total_vol_a) > V) {
		return true;
	}	

	if (total_temp > V*X) {
		double new_V = V;
		double new_X;
		for (int i = 0; i < N; ++i) {
			if (C[i] < X) {
				new_V -= t*R[i];

			}
		}
	} else if (total_temp < V*X) {
	} else {
		return true;
	}
}*/

int main() {
	cout.precision(15);

	int t, T;
	cin >> T;
	for (t = 0; t < T; ++t) {
		int N;
		double V, X;
		cin >> N >> V >> X;

		vector<double> R(N), C(N);

		for (int i = 0; i < N; ++i) {
			cin >> R[i] >> C[i];
		}


		cout << "Case #" << (t+1) << ": ";

		if (fabs(C[0]-C[1]) < EPS) {
			R[0] += R[1];
			N = 1;
		}

		if (N == 1) {
			if (fabs(C[0]-X) < EPS) {
				cout << V/R[0] << endl;
				continue;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		}

		if (N == 2) {
			double t1 = V*(C[0]-X)/(R[1]*(C[0]-C[1]));
			double t2 = V*(C[1]-X)/(R[0]*(C[1]-C[0]));

			if ((t1 < 0) || (t2 < 0)) {
				cout << "IMPOSSIBLE" << endl;				
			} else {
				cout << max(t1, t2) << endl;
			}
			continue;
		}

		
		

	}
	return 0;
}