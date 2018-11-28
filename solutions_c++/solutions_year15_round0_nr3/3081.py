// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

array<array<int, 4>, 4> lut = { {
	{ 0, 1, 2, 3 },
	{ 1, 4, 3, 6 },
	{ 2, 7, 4, 1 },
	{ 3, 2, 5, 4 },
	} };

int mult(int x, int y){
	int r1 = lut[x & 3][y & 3];
	if (x > 3) r1 ^= 4;
	if (y > 3) r1 ^= 4;
	return r1;
}

int main(){
	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++){
		int L, X;
		cin >> L >> X;
		string ls;
		cin >> ls;
		vector<int> pat(L);
		for (int i = 0; i < L; i++){
			pat[i] = ls[i] - 'i' + 1;
		}
		vector<int> state(L*X);
		for (int i = 0; i < X; i++){
			copy(pat.begin(), pat.end(), state.begin() + L*i);
		}
		bool ans = false;
		//init check
		int bs = 0;
		for (int i = 0; i < X*L; i++){
			bs = mult(bs, state[i]);
		}
		if (bs != 4) goto opt;
		bs = 0;
		for (int i = 0; i < X*L - 2; i++){
			bs = mult(bs, state[i]);
			if (bs == 1){
				int cs = 0;
				for (int j = i + 1; j < X*L - 1; j++){
					cs = mult(cs, state[j]);
					if (cs == 2){
						ans = true;
						goto opt;
					}
				}
			}
		}
	opt:
		cout << "Case #" << tt + 1 << ": " << (ans ? "YES" : "NO") << endl;
	}
	return 0;
}


