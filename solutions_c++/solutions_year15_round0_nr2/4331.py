#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <windows.h>

using namespace std;

string str;



int main() {
	//freopen("output.txt", "w", stdout);
	int q;
	int j = 1;
	cin >> q;
	for (; q > 0; --q) {
		int p;
		vector<int> in;
		cin >> p;
		in.resize(p);
		int mxIn = 0;
		for (int i = 0; i < p; ++i) {
			cin >> in[i];
			mxIn = max(mxIn, in[i]);
		}
		int ans = mxIn;
		for (int mx = 1; mx <= mxIn; ++mx) {
			int tans = mx;
			for (int i = 0; i < p; ++i) {
				tans += (in[i] - 1) / mx;
			}
			ans = min(ans, tans);
		}
		cout << "Case #" << j << ": " << ans << endl;
		j++;
	}
	
}