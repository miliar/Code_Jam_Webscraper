#include <iostream>
#include <vector>
using namespace std;

int N;
int dp[1000000][100];
char operates[100][100];
bool visited1[100];
bool visited2[100];
int iterate[100];

pair<int, int> recurse2(int j);

pair<int, int> recurse1(int i) {
	if (visited1[i]) return {0,0};
	visited1[i] = true;

	pair<int, int> ret = {1,0};
	for (int j = 0; j < N; j++) {
		if (operates[i][j] == '0') continue;
		pair<int, int> more = recurse2(j);
		ret.first += more.first;
		ret.second += more.second;
	}
	return ret;
}

pair<int, int> recurse2(int j) {
	if (visited2[j]) return {0,0};
	visited2[j] = true;

	pair<int, int> ret = {0,1};
	for (int i = 0; i < N; i++) {
		if (operates[i][j] == '0') continue;
		pair<int, int> more = recurse1(i);
		ret.first += more.first;
		ret.second += more.second;
	}
	return ret;
	
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N;

		int starting = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> operates[i][j];
				starting += operates[i][j]-'0';
			}
			visited1[i] = visited2[i] = false;
		}

		vector<pair<int, int>> pieces;
		int useless = 0;
		for (int i = 0; i < N; i++) {
			if (visited1[i]) continue;

			pair<int, int> piece = recurse1(i);
			if (piece.second == 0) {
				useless++;
			} else if (piece.first == piece.second) {
				starting -= piece.first*piece.first;
			} else {
				pieces.push_back(piece);
			}
		}

		int P = pieces.size();
		

		for (int k = 0; k < (1<<P); k++) {
			for (int z = 0; z <= useless; z++) {
				dp[k][z] = 1000000;
			}
		}

		for (int c = 0; c < P; c++) {
			iterate[c] = 0;
		}

		dp[0][useless] = 0;
		for (;;) {
			bool dead = true;
			for (int c = 0; c < P; c++) {
				if (iterate[c] < 2) {
					iterate[c]++;
					dead = false;
					break;
				}
				iterate[c] = 0;
			}
			if (dead) break;

			int oldstate = 0, newstate = 0, size1 = 0, size2 = 0;
			for (int c = 0; c < P; c++) {
				if (iterate[c] > 0) newstate += (1<<c);
				if (iterate[c] > 1) oldstate += (1<<c);
				if (iterate[c] == 1) {
					size1 += pieces[c].first;
					size2 += pieces[c].second;
				}
			}
			if (oldstate == newstate) continue;

			int uselessused = (size1 < size2 ? size2-size1 : 0);
			int cost = size1+uselessused;
			for (int z = uselessused; z <= useless; z++) {
				if (dp[oldstate][z]+cost*cost < dp[newstate][z-uselessused]) {
					dp[newstate][z-uselessused] = dp[oldstate][z]+cost*cost;
				}
			}
		}

		int best = 1000000;
		for (int z = 0; z <= useless; z++) {
			if (dp[(1<<P)-1][z]+z < best) {
				best = dp[(1<<P)-1][z]+z;
			}
		}
		cout << "Case #" << t << ": " << best-starting << '\n';
	}

	return 0;
}
