										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n;
bool ini[5][5];
bool mat[5][5];

int main(){
	freopen("D-Freeform Factory.in", "r", stdin);
	freopen("D-Freeform Factory.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n;
		string str;
		for(int i = 0; i < n; i++){
			cin >> str;
			for(int j = 0; j < n; j++)
				ini[i][j] = str[j] - '0';
		}
		int m = n * n;
		int res = m;
		for(int mask = 0; mask < (1 << m); mask++){
			for(int i = 0; i < m; i++)
				mat[i / n][i % n] = (mask >> i) & 1;

			int cnt = 0;
			bool ok = true;
			int r[5] = {}, c[5] = {};
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					if(ini[i][j] && !mat[i][j])
						ok = false;
					if(mat[i][j]){
						r[i]++, c[j]++;
						if(!ini[i][j])
							cnt++;
					}
				}
			}

			for(int i = 0; i < n; i++)
				if(!r[i] || !c[i])
					ok = false;
			if(!ok) continue;
			
			int same[5] = {};
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++){
					bool a = false, b = false;
					for(int k = 0; k < n; k++){
						if(mat[i][k] && mat[j][k])
							a = true;
						if(mat[i][k] != mat[j][k])
							b = true;
					}
					if(a && b)
						ok = false;
					if(a) same[i]++;
				}
				if(same[i] != r[i])
					ok = false;
			}
			if(!ok) continue;
			/*cout << cnt << endl;
			for(int i = 0; i < n; i++)
				cout << r[i] << ' ';
			cout << endl;
			for(int i = 0; i < n; i++)
				cout << c[i] << ' ';
			cout << endl;
			for(int i = 0; i < n; i++)
				cout << same[i] << ' ';
			cout << endl;
			for(int i = 0; i < n; i++){
				for(int j = 0; j < n; j++)
					cout << mat[i][j] << ' ';
				cout << endl;
			}
			*/
			res = min(res, cnt);
		}
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}
