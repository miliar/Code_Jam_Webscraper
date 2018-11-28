#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T, R, N, M, K;
	cin >> T >> R >> N >> M >> K;
	cout << "Case #1:" << endl;
	for (int r=0; r<R; ++r) {
		vector<int> tt(9);
		for (int i=0; i<K; ++i) {
			int w;
			cin >> w;
			vector<int> t(9);
			for (int m=M; m>=2; --m) while (w%m==0) { 
				t[m] ++;
				w /= m;
			}
			for (int j=0; j<9; ++j) tt[j] = max(tt[j], t[j]);
		}
		vector<int> out;
		for (int i=8; i>=2 && out.size() < N; --i) {
			while (tt[i] && out.size() < N) {
				out.push_back(i);
				tt[i]--;
			}
		}
		while(out.size() < N) out.push_back(2);
		for (int i=0; i<N; ++i) cout << out[i]; cout << endl;
	}
	return 0;
}