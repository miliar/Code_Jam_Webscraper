#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	int N, K;
	cin >> N >> K;
	
	vector<double> prob(N);
	for (int i=0; i<N; i++) cin >> prob[i];
	sort(prob.begin(), prob.end());
	
	double best = 0.0;
	
	for (int l = 0; l<=K; l++) {
		vector<double> chance(N+1,0);
		chance[0] = 1.0;
		for (int i=0; i<l; i++) {
			vector<double> nchance(N+1, 0);
			for (int k=0; k<N; k++) {
				nchance[k] += chance[k]*(1.0-prob[i]);
				nchance[k+1] += chance[k]*prob[i];
			}
			nchance.swap(chance);
		}
		for (int i=0; i<K-l; i++) {
			vector<double> nchance(N+1, 0);
			for (int k=0; k<N; k++) {
				nchance[k] += chance[k]*(1.0-prob[N-i-1]);
				nchance[k+1] += chance[k]*prob[N-i-1];
			}
			nchance.swap(chance);
		}
		best = max(best, chance[K/2]);
	}
	cout << "Case #" << t << ": " << setprecision(10) << best << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++) doCase(i+1);
	return 0;
}
