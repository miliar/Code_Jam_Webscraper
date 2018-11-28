#include <iostream>
#include <cstdio>
using namespace std;

int M, N;
int lawn[100 + 1][100 + 1];

bool checkHorizontal(int i, int j) {
	for (int k = 0; k < N; k++) {
		if (lawn[i][k] > lawn[i][j]) return false;
	}
	return true;
}

bool checkVertical(int i, int j) {
	for (int k = 0; k < M; k++) {
		if (lawn[k][j] > lawn[i][j]) return false;
	}
	return true;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int testCases;
	cin >> testCases;
	for (int testCase = 1; testCase <= testCases; testCase++) {
		cin >> M >> N;
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++)
				cin >> lawn[i][j];
		
		bool isPossible = true;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				isPossible &= (checkHorizontal(i, j) | checkVertical(i, j));
				
				if (!isPossible) break;
			}
			if (!isPossible) break;
		}
		cout << "Case #" << testCase << ": " << (isPossible ? "YES" : "NO") << endl;
	}
	return 0;
}
