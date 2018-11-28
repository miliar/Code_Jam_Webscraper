#include<iostream>
#include<string>
#include<vector>

using namespace std;

int readBoolList(vector<bool>& boolList) {
	string boolString;
	int K;
	cin >> boolString >> K;
	for (auto& ch : boolString) {
		if (ch == '-') boolList.push_back(false);
		else boolList.push_back(true);
	}
	return K;
}

void flipKConsecutive(int i, int K, vector<bool>& boolList) {
	for (int j = i; j < K + i; ++j) {
		boolList[j] = !boolList[j];
	}
}

bool checkFlippedList(int K, int N, vector<bool>& boolList) {
	for (int i = N - K; i < N; ++i) {
		if (!boolList[i]) return false;
	}
	return true;
}

int findFlips(int K, int N, vector<bool>& boolList) {
	int numberOfFlips = 0;
	for (int i = 0; i <= N-K; ++i) {
		if (!boolList[i]) {
			flipKConsecutive(i, K, boolList);
			++numberOfFlips;
		}
	}
	if (checkFlippedList(K,N,boolList)) return numberOfFlips;
	else return -1;
}

int main() {
	int T;
	cin >> T;
	
	for (int i = 1; i <= T; ++i) {
		vector<bool> boolList;
		int K = readBoolList(boolList);
		int N = boolList.size();

		int flips = findFlips(K, N, boolList);
		cout << "case #" << i << ": ";
		if (flips == -1) cout << "IMPOSSIBLE\n";
		else cout << flips << '\n';
	}
}