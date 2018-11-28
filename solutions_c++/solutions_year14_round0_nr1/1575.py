#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int a, b, x[4][4], y[4][4];
		cin >> a; a--;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) cin >> x[i][j];
		cin >> b; b--;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) cin >> y[i][j];
		int c = 0, v = -1;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(x[a][i] == y[b][j]){
					v = x[a][i];
					c++;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if(c == 0) cout << "Volunteer cheated!\n";
		else if(c == 1) cout << v << '\n';
		else cout << "Bad magician!\n";
	}
}