#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string tour[13][3];
		int count[13][3][3];
		tour[0][0] = "R"; // R wins
		tour[0][1] = "P"; // P
		tour[0][2] = "S"; // S
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				count[0][i][j] = 0;
			}
			count[0][i][i] = 1;
		}
		for(int i = 1; i <= 12; i++){
			for(int j = 0; j < 3; j++){
				for(int k = 0; k < 3; k++){
					count[i][j][k] = count[i-1][j][k] + count[i-1][(j+2)%3][k];
				}
				string a = tour[i-1][j];
				string b = tour[i-1][(j+2)%3];
				for(int z = 0; z < a.size(); z++){
					if(a[z] < b[z]){
						break;
					} else if(a[z] > b[z]){
						swap(a,b);
						break;
					}
				}
				tour[i][j] = a + b;
			}
		}
		int yes = 0;
		for(int j = 0; j < 3; j++){
			if(count[n][j][0] == r && count[n][j][1] == p && count[n][j][2] == s){
				cout << tour[n][j] << endl;
				yes = 1;
			}
		}
		if(!yes){
			printf("IMPOSSIBLE\n");
		}
	}
	exit(0);
}