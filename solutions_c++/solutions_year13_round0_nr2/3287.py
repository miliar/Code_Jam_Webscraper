#include <iostream>
using namespace std;
int n, m, mx;
int c[101][101];
bool proc(){
	for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j){
			if (c[i][j] == mx)
				continue;
			bool check = false;
			bool flag = true;
			for (int k=0; k<m; ++k){
				if (c[i][k] > c[i][j]) {
					flag = false;
					break;
				}
			}
			if (flag) check = true;
			flag = true;
			for (int k=0; k<n; ++k){
				if (c[k][j] > c[i][j]) {
					flag = false;
					break;
				}
			}
			if (flag) check = true;
			if (!check) return false;
		}
	return true;
}
int main(){
	int t; cin >> t;
	for (int cas=1; cas<=t; ++cas){
		cin >> n >> m; mx = 0;
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j){
				cin >> c[i][j];
				mx = mx > c[i][j] ? mx : c[i][j];
			}
		cout << "Case #" << cas << ": " << (proc()?"YES":"NO") << endl;
	}
}