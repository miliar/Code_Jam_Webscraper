#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <assert.h>
#include <queue>

using namespace std;

bool guaranteed(const vector<vector<int>>& D)
{
	const int N = D.size();
	vector<int> zzz(N, 0);
	vector<int> qqq(N, 0);
	for (int i = 0; i < N; i++) {
		// ѕеребираем рабочих.
		// Ќа каких станках может работать рабочий.
		vector<int> xxx(N, 0);
		int targetCount = 0;
		for (int j = 0; j < N; j++) {
			if (D[i][j] == 1) {
				xxx[j] = 1;
				// Ќа этом станке может работать хот€ бы один рабочий
				zzz[j] = 1;
				// Ётот рабочий работает хот€ бы на одном станке.
				qqq[i] = 1;
				targetCount++;
			}
		}
		// »щем других рабочих, которые работают хот€ бы на одном из этих станков.
		int otherGoodCount = 0;
		for (int k = 0; k < N; k++) {
			if (k == i) continue;
			bool isGood = false;
			for (int j = 0; j < N; j++) {
				if (xxx[j] == 1 && D[k][j] == 1) {
					isGood = true;
					break;
				}
			}
			if (isGood) {
				// —мотрим, на каких станках ещЄ может работать этот рабочий.
				vector<int> yyy(N, 0);
				for (int j = 0; j < N; j++) {
					if (D[k][j] == 1) {
						yyy[j] = 1;
					}
				}
				// „тобы матрица была хорошей, xxx и yyy должны совпадать.
				for (int j = 0; j < N; j++) {
					if (xxx[j] != yyy[j]) {
						return false;
					}
				}
				otherGoodCount++;
			}
		}
		// ƒругих рабочих должно быть ровно столько же, сколько станков - 1.
		if (targetCount != otherGoodCount + 1) {
			return false;
		}
	}
	// ѕровер€ем, что на всех станках кто-то может работать.
	for (int j = 0; j < N; j++) {
		if (zzz[j] == 0) {
			return false;
		}
	}
	// ѕровер€ем, что все работают
	for (int i = 0; i < N; i++) {
		if (qqq[i] == 0) {
			return false;
		}
	}
	return true;
}

void test()
{
	int N;
	cin >> N;
	vector<vector<int>> D(N, vector<int>(N, 0));
	vector<vector<int>> DD(N, vector<int>(N, 0));
	for (int i = 0; i < N; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < N; j++) {
			D[i][j] = s[j] == '1' ? 1 : 0;
		}
	}

	bool res = guaranteed({
		{ 0, 0, 0 },
		{ 1, 1, 0 },
		{ 0, 0, 0 },
	});

	int nn = N * N;
	int maskMax = 1 << nn;
	int result = INT_MAX;
	for (int mask = 0; mask < maskMax; mask++) {
		bool skip = false;
		int cost = 0;
		DD = D;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int bit = 1 << (N * i + j);
				if ((mask & bit) != 0) {
					if (D[i][j] == 1) {
						skip = true;
						break;
					} else {
						DD[i][j] = 1;
						cost++;
					}
				}
			}
			if (skip) break;
		}
		if (skip) continue;

		if (guaranteed(DD)) {
			result = min(result, cost);
		}
	}
	cout << result;
}

int main()
{
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
