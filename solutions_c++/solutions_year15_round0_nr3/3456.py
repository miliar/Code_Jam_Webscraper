#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;


int main() {
	char TAB[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2} ,{4, 3, -2, -1}};
	int tc;
	cin >> tc;
	int c = 1; 
	while( c <= tc){
		bool ans = false;
		int l, x;
		cin >> l >> x;
		int len = l*x;
		char T[10001], S[10001];
		cin >> T;
		strcpy(S, T);
		for(int i = 1; i<x; i++)
			strcat(S, T);
		//cout << S << endl;
		int ptr = 0;
		int pre = 1;
		bool flag_i = false, flag_j = false, flag_k = false;
		for(int i = 0; i<len; i++) {
			if(flag_i == false) {
				int val = TAB[abs(pre)-1][S[i] - 'i' + 1];
				if(pre < 0) val = -val;
				pre = val;
				if(val == 2) {
					flag_i = true;
					pre = 1;
					//cout << "F I" << endl;
				}
			}
			else if( flag_j == false) {
				int val = TAB[abs(pre)-1][S[i] - 'i' + 1];
				if(pre < 0) val = -val;
				pre = val;
				if(val == 3) {
					flag_j = true;
					pre = 1;
					//cout << "F J" << endl;
				}
			}
			else if( flag_k == false) {
				int val = TAB[abs(pre)-1][S[i] - 'i' + 1];
				if(pre < 0) val = -val;
				pre = val;
				//cout << val << endl;
				if(val == 4) {
					flag_k = true;
					pre = 1;
					//cout << "F K" << endl;
					if( i == len-1){
						ans = true;
					}
				}
			}
			else {
				pre = 1;
				int val = 1;
				for(; i<len; i++) {
					val = TAB[abs(pre)-1][S[i] - 'i' + 1];
					if(pre < 0) val = -val;
					//cout << val << endl;
					pre = val;
				}
				if(val == 1)
					ans = true;
			}
		}
		if(ans == true)
			cout << "Case #" << c << ": YES"<< endl;
		else
			cout << "Case #" << c << ": NO"<< endl;
		c++;
	}
}