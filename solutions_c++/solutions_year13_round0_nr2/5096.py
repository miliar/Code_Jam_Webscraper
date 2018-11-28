#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
using namespace std;

bool func(vector<vector<int> > &lawn, int N, int M) {
	vector<vector<bool> > mark(N, vector<bool>(M, false));
	vector<int> rht(N, INT_MIN);
	vector<int> cht(M, INT_MIN);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			rht[i] = max(rht[i], lawn[i][j]);
			cht[j] = max(cht[j], lawn[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (lawn[i][j] == rht[i] || lawn[i][j] == cht[j]) {
				mark[i][j] = true;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (false == mark[i][j]) {
				return false;
			}
		}
	}	
	return true;		
}

void solve() {
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T = 0;
	in >> T;
	
	for (int t = 1; t <= T; t++) {
		int N, M;
		in >> N;
		in >> M;
		vector<vector<int> > lawn(N, vector<int>(M));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				in >> lawn[i][j];
			}
		}		
		bool res = func(lawn, N, M);	
		out << "Case #" << t << ": " << (res == true? "YES" : "NO") << endl;
	}	
	in.close();
	out.close();
}

int main() {
	solve();
	return 0;	
}
