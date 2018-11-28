#include<iostream>
#include<vector>

using namespace std;

void checkPossible() {
	int N, M;
	//N = rows, M = columns
	cin >> N >> M;
	int lawn[N][M];
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			cin >> lawn[i][j];
	vector<int> columnMax;
	vector<int> rowMax;
	columnMax.resize(M);
	rowMax.resize(N);
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < M; j++) {
			if(lawn[i][j] > rowMax[i])
				rowMax[i] = lawn[i][j];
			if(lawn[i][j] > columnMax[j])
				columnMax[j] = lawn[i][j];
		}
	}
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			if(lawn[i][j] < rowMax[i] && lawn[i][j] < columnMax[j]) {
				cout << "NO";
				return;
			}
	cout << "YES";	
}

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ": ";
		checkPossible();
		cout << endl;
	}
	return 0;
}
