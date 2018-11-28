#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int count = 1; count <= T; count++) {
		int a, b;
		int o[4][4] = {0}, f[4][4] = {0};
		cin >> a; a--;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) cin >> o[i][j];
		cin >> b; b--;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) cin >> f[i][j];
		vector<int> c;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(o[a][i] == f[b][j])
					c.push_back(o[a][i]);
		cout << "Case #" << count << ": ";
		if(c.empty()) cout << "Volunteer cheated!" << endl;
		else if(c.size() > 1) cout << "Bad magician!" << endl;
		else cout << c[0] << endl;
	}
}
