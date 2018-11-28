#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <fstream>
using namespace std;

int war(vector<double> n, vector<double> k) {
	int sk = 0;
	for (int i = 0; i < n.size(); i++) {
		//if (n[i] == -1) continue;
		for (int j = 0; j < k.size(); j++) {
			if (k[j] == -1) continue;
			if (k[j] > n[i]) {
				k[j] = -1;
				sk++;
				break;
			}
		}
	}
	return k.size()-sk;
}

int dwar(vector<double> n, vector<double> k) {

	int count = 0;
	int j = 0;
	for (int i = 0; i < n.size(); i++) {
		if (n[i] < k[j])  {
			k.pop_back();
		} else {
			count++;
			j++;
		}
	}
	return count;
}

int main() {
	int T;
	cin >> T;
	ofstream out("war.txt");
	for (int idx = 1; idx <= T; idx++) {
		int N;
		cin >> N;
		vector<double> naomi(N), ken(N);

		for (int i = 0; i < N; i++) cin >> naomi[i];
		for (int i = 0; i < N; i++) cin >> ken[i];

		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		
		out << "Case #" << idx << ": " << dwar(naomi,ken) << " " << war(naomi,ken);
		if (idx != T) out << endl;
	}

	return 0;
}