#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int t, n, nao_d, nao_w;
vector<double> nao, ken;

int game(vector<double> a, vector<double> b) {
	int r = 0;
	for (int i = 0; i < n; i++) {
		double k_s = a[a.size() - 1];
		int n_i = -1;
		for (int j = b.size()-1; j >= 0; j--) {
			if (b[j] > k_s) {
				n_i = j;
			}
		}
		a.pop_back();
		if (n_i != -1) {
			b.erase(b.begin()+n_i);
			r++;
		}
		else {
			b.erase(b.begin());
		}
	}
	return r;
}

int main() {
	ifstream fin ("D-large.in");
	ofstream fout ("war.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> n;
		double na[n], ke[n];
		for (int j = 0; j < n; j++) {
			fin >> na[j];
		}
		for (int j = 0; j < n; j++) {
			fin >> ke[j];
		}
		sort(na, na+n);
		sort(ke, ke+n);
		nao.insert(nao.begin(), na, na+n);
		ken.insert(ken.begin(), ke, ke+n);
		nao_d = game(ken, nao);
		nao.clear();
		ken.clear();

		nao.insert(nao.begin(), na, na+n);
		ken.insert(ken.begin(), ke, ke+n);
		nao_w = game(nao, ken);
		nao.clear();
		ken.clear();
		nao_w = n - nao_w;
		fout << "Case #" << i << ": " << nao_d << " " << nao_w << endl;
	}
}
