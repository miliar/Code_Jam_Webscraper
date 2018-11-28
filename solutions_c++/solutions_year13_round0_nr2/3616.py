#include <iostream>
using namespace std;

int G[100][100];
int N, M;

int check_col(int i, int j) {
	int k;
	for(k = 0; k < M; k++)
		if(G[i][k] > G[i][j]) 
			return 0;
	return 1;
}

int check_row(int i, int j) {
	int k;
	for(k = 0; k < N; k++)
		if(G[k][j] > G[i][j]) 
			return 0;
	return 1;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int i, j;
	int T, t;
	int flag;

	cin >> T;
	for(t = 1; t < T + 1; t++) {
		cin >> N >> M;
		for(i = 0; i < N; i++)
			for(j = 0; j < M; j++)
				cin >> G[i][j];
		flag = 1;
		for(i = 0; i < N && flag == 1; i++) 
			for(j = 0; j < M && flag == 1; j++) 
				if(!(check_col(i, j) || check_row(i, j)))
					flag = 0;
		if(flag == 1) cout << "Case #" << t << ": " << "YES" << endl;
		else cout << "Case #" << t << ": " << "NO" << endl;
				
	}
	return 0;
}