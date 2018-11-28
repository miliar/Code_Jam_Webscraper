#include <iostream>
#include <cstdio>
using namespace std;

int h[200][200];

int main(){
	int T;
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas++){
		bool able = true;
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			cin >> h[i][j];
		cout << "Case #" << cas << ": ";
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			if(h[i][j] > 100 && h[i][j] < 1) able = false;
			
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++){
				bool mow = false, line = true;
				for(int k = 0; k < n; k++)
					line = line && (h[i][j] >= h[k][j]);
				mow = mow || line; line = true;
				for(int k = 0; k < m; k++)
					line = line && (h[i][j] >= h[i][k]);
				mow = mow || line;
				able = able && mow;
			}
		if(able) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}