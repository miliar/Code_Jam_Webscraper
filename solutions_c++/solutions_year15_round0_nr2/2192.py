#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int d[1001][1001];
int m[1001][1001];

int calc(int i, int j) {
	if (d[i][j] != -1)
		return d[i][j];
	if (i <= j) {
		d[i][j] = 0;
		m[i][j] = i;
		return 0;
	}
	int mint = 9999;
	int mm = 0;
	for (int k=1;k<=i/2;k++) {
		int time = calc(k, j) + calc(i - k, j) + 1;
		if (mint > time) {
			mint = time;
			mm = max(m[k][j], m[i-k][j]);
		}
	}
	d[i][j] = mint;
	m[i][j] = mm;
	return d[i][j];
}
int main() {
	int T;
	cin >> T;
	memset(d, -1, sizeof(d));

	for (int i=1;i<=1000;i++) {
		for (int j=1;j<=1000;j++) {
			if (d[i][j] == -1)
				calc(i, j);
		}
	}
	for (int t=1;t<=T;t++) {
		
		int D;
		cin >> D;

		vector<int> p;

		int maxt = 0;
		for (int i=0;i<D;i++) {
			int pc;
			cin >> pc;
			p.push_back(pc);
			if (maxt < pc) maxt = pc;
		}

		int mint = 1111;
		int maxe = 0;
		for (int i=1;i<=maxt;i++) {
			int time = 0;	
			for (int j=0;j<p.size();j++) {
				time += d[p[j]][i];
				if (maxe < m[p[j]][i]) {
					maxe = m[p[j]][i];
				}
			}
			//cout << time << ", " << maxe << endl;
			if (mint > time + maxe) {
				mint = time + maxe;
			}
		}

		cout << "Case #" << t << ": " << mint << endl;
		
	}
	return 0;
}
