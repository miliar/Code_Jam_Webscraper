#include <iostream>

using namespace std;

char q[101][101];

int main(){
	int T;
	cin >> T;
	for (int k = 1; k <= T; k++){
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++){
			cin >> q[i][j];
			
		}
		int ans = 0;
		bool ok = true, f;
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (q[i][j] == '.') continue;
				if (q[i][j] == '^'){
					f = false;
					for (int l = i - 1; l >= 0; l--){
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ans++;
					for (int l = i + 1; l < r; l++){
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = j + 1; l < c; l++){
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = j - 1; l >= 0; l--){
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ok = false;
				}
				else if (q[i][j] == '>'){
					f = false;
					for (int l = j + 1; l < c; l++){ //you
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ans++;
					for (int l = i + 1; l < r; l++){ //xia
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = i - 1; l >= 0; l--){ //shang
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = j - 1; l >= 0; l--){ //zuo
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ok = false;
				}
				else if (q[i][j] == 'v'){
					f = false;
					for (int l = i + 1; l < r; l++){ //xia
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ans++;
					for (int l = j + 1; l < c; l++){ //you
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = i - 1; l >= 0; l--){ //shang
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = j - 1; l >= 0; l--){ //zuo
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ok = false;
				}
				else if (q[i][j] == '<'){
					f = false;
					for (int l = j - 1; l >= 0; l--){ //zuo
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ans++;
					for (int l = j + 1; l < c; l++){ //you
						if (q[i][l] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = i - 1; l >= 0; l--){ //shang
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					for (int l = i + 1; l < r; l++){ //xia
						if (q[l][j] == '.') continue;
						f = true;
						break;
					}
					if (f) continue;
					ok = false;
				}
				if (!ok) break;
			}
		}
		if (ok) cout << "Case #" << k << ": " << ans << endl;
		else cout << "Case #" << k << ": IMPOSSIBLE" << endl;
	}
	
	return 0;
} 
