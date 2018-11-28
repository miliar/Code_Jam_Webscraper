#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> getTroie(int K, int C);
long long troiaToPosition(const vector<int> &troie, const int K);
long long llPow(long long base, int exp);

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		int K, C, S;
		cin >> K >> C >> S;

		cout << "Case #" << t << ":";

		auto troie = getTroie(K, C);
		if(troie.size() > static_cast<unsigned>(S)) cout << " IMPOSSIBLE";
		else {
			for(auto p : troie) {
				cout << " " << troiaToPosition(p, K);
			}
		}
		cout << "\n";
	}

	return 0;
}


vector<vector<int>> getTroie(int K, int C)
{
	vector<vector<int>> res;
	
	long long currentT = 0;
	while(currentT < K) {
		vector<int> partial(C);

		for(int i = 0; i < C; i++) {
			if(currentT >= K) currentT = K-1;
			partial[i] = currentT;
			currentT++;
		}

		res.push_back(partial);
	}

	return res;

}

long long troiaToPosition(const vector<int> &troia, const int K)
{
	long long res = 0;

	for(unsigned i = 0; i < troia.size(); i++) {
		res *= K;
		res += troia[i];
	}

	return res + 1;
}

long long llPow(long long base, int exp)
{
	long long res = 1;
	while(exp--) {
		res *= base;
	}

	return res;
}