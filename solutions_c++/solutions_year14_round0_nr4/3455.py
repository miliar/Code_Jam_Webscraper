#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int playWar(vector<double> &naomi, vector<double> &ken) {
	int pts = 0;
	int ptKen = 0;

	for (int ptNao = 0; ptNao < naomi.size(); ++ptNao) {
		if (naomi[ptNao] > ken[ptKen]) {
			++pts;
		} else {
			++ptKen;
		}
	}

	return pts;
}

int playDecWar(vector<double> &naomi, vector<double> &ken) {
	int pts = 0;
	int ptNao = 0;

	for (int ptKen = 0; ptKen < ken.size(); ++ptKen) {
		if (ken[ptKen] < naomi[ptNao]) {
			++ptNao;
			++pts;
		}
	}

	return pts;
}

int main() {
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		int N;
		cin >> N;

		vector<double> naomi(N);
		vector<double> ken(N);

		for (int i = 0; i < N; ++i) cin >> naomi[i];
		for (int i = 0; i < N; ++i) cin >> ken[i];

		sort(naomi.begin(), naomi.end(), greater<double>());
		sort(ken.begin(), ken.end(), greater<double>());

		int decWar = playDecWar(naomi, ken);
		int war = playWar(naomi, ken);

		cout << "Case #" << cn << ": " << decWar << " " << war << endl; 
	}
}