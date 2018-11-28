#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

string x[101];
int RR[101], CC[101];
bool z[101][101];

int main() {
	int T;
	cin >> T;
	for (int times = 1; times <= T; ++times) {
	    int R, C;
		cin >> R >> C;
		for (int i = 0; i < R; ++i) cin >> x[i];
		memset(z, 0, sizeof(z));
		memset(RR, 0, sizeof(RR));
		memset(CC, 0, sizeof(CC));
	//	cout << x[0] << endl;
		int NN = 0;
		for (int i = 0; i < R; ++i)
		 for (int j = 0; j < C; ++j) 
    		 if (x[i][j] != '.') {
			     ++NN;
				 ++RR[i];
				 ++CC[j];
			}
		if (NN == 0) {
		    cout << "Case #" << times << ": 0" << endl;
			continue;
		}
		
		bool flag = true;
		for (int i = 0; i < R; ++i)
		 for (int j = 0; j < C; ++j) 
    		 if (x[i][j] != '.') 
			     if (RR[i] == 1 && CC[j] == 1) {
				     flag = false;
				 }
		if (!flag) {
		    cout << "Case #" << times << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		int ans = 0;
		for (int i = 0; i < R; ++i) {
		    if (RR[i] == 0) continue;
			int j = 0;
			while (x[i][j] == '.') ++j;
			if (x[i][j] == '<') {
			    if (!z[i][j]) ++ans;
				z[i][j] = true;
			}
			j = C - 1;
			while (x[i][j] == '.') --j;
			if (x[i][j] == '>') {
			    if (!z[i][j]) ++ans;
				z[i][j] = true;
			}
		}
		for (int j = 0; j < C; ++j) {
		    if (CC[j] == 0) continue;
			int i = 0;
			while (x[i][j] == '.') ++i;
			if (x[i][j] == '^') {
			    if (!z[i][j]) ++ans;
				z[i][j] = true;
			}
			i = R - 1;
			while (x[i][j] == '.') --i;
			if (x[i][j] == 'v') {
			    if (!z[i][j]) ++ans;
				z[i][j] = true;
			}
		}
		cout << "Case #" << times << ": " << ans << endl;
	}
    return 0;
}