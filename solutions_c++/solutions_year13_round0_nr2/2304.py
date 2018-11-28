#include <ctime>
#include <cstdio>
#include <iostream>

using namespace std;

const int cmax = 10;

int n, m;
int mat[cmax][cmax];

void run(){
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> mat[i][j];
	for (int mask = 0; mask < (1 << (n + m)); mask++){
		bool flag = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				int value = (mask & (1 << i)) || (mask & (1 << (n + j))) ? 1 : 2;
				if (mat[i][j] != value){
					flag = false;
					break;
				}
			}
		if (flag){
			cout << "YES\n";
			return ;
		}
	}
	cout << "NO\n";
}

int main(){
	int t; cin >> t;
	for (int i = 0; i < t; i++){
		double begin = clock();
		printf("Case #%d: ", i + 1);
		cerr << "Starting solving case " << i << endl;
		run();
		cerr << i + 1 << "OK!" << endl;
		cerr << "Time elapsed: " << fixed << (clock() - begin) / CLOCKS_PER_SEC << endl;
	}
}