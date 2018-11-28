#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> Vi;
typedef vector<Vi > Mi;

bool check(Mi & ma) {
	Vi rows(ma.size(),1);
	Vi cols(ma[0].size(),1);
	for(int i = 0; i < ma.size(); ++i) {
		for(int j = 0; j < ma[i].size(); ++j) {
			if(ma[i][j] > rows[i]) rows[i] = ma[i][j];
			if(ma[i][j] > cols[j]) cols[j] = ma[i][j];
		}
	}
	for(int i = 0; i < ma.size(); ++i) {
		for(int j = 0; j < ma[i].size(); ++j) {
			if(ma[i][j] < rows[i] and ma[i][j] < cols[j]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int n,m;
		cin >> n >> m;
		Mi ma(n,Vi(m));
		for(int j = 0; j < n; ++j) {
			for(int k = 0; k < m; ++k) {
				cin >> ma[j][k];
			}
		}
		if(check(ma)) {
			cout << "Case #"<< i+1 << ": YES" << endl;
		} else {
			cout << "Case #"<< i+1 << ": NO" << endl;
		}
	}
}