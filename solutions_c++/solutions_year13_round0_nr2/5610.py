#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for(int t = 0; t < T; t++){
		int n, m;
		cin >> n >> m;
		int a[n][m];

		int _max = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> a[i][j];
				_max = max(a[i][j], _max);
			}
		}

		bool flag = true;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(_max == a[i][j]) continue;

				bool all_same_column = true;
				for(int k = 0; k < n; k++){
					if(a[i][j] != a[k][j]) all_same_column = false;
				}

				bool all_same_row = true;

				for(int k = 0; k < m; k++){
					if(a[i][j] != a[i][k]) all_same_row = false;
				}

				flag &= (all_same_row | all_same_column);
			}
		}

		cout << "Case #" << t+1 << ": " ;
		if(flag){
			cout << "YES\n";
		}else{
			cout << "NO\n";
		}

	}
	return 0;
}
