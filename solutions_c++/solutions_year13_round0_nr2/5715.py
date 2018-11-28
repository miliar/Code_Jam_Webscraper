#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T,g[10][10],N,M;
	bool f1,f2;
	cin >> T;
	for (int t = 0; t < T; t++){
		cin >> N >> M;
		cout << "Case #" << t+1 << ": ";
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++){
				cin >> g[i][j];
			}
		}
		for (int i = 0; i < N; i++){
			for (int j = 0; j < M; j++){
				if (g[i][j]==2) continue;
				//row check
				f1=true,f2=true;
				for (int k = 0; k < M; k++){
					f1=true;
					if (g[i][k]!=g[i][j]){
						f1=false;
						break;
					}
				}
				//col check
				for (int k = 0; k < N; k++){
					f2=true;
					if (g[k][j]!=g[i][j]){
						f2=false;
						break;
					}
				}
				if (!f1&&!f2) {
					cout << "NO" << endl;
					goto done;
				}
			}
		}
		cout << "YES" << endl;
		done:;
		
	}
	return 0;
}
