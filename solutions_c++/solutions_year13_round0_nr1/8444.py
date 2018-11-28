#include<iostream>
#include<list>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<utility>
#include<list>
#include<set>
#include<map>
#include<bitset>
#include<vector>
#include<algorithm>
#include<bitset>
#include <deque>
#include<limits>
#include<string>
#include<cstring>
#include<cctype>
#include<iomanip>
#include<sstream>
#include<fstream>

using namespace std;

int main(){
	unsigned int T;
	cin >> T;
	unsigned int t = 0;

	while(T--){

		bool xw = false, ow = false, dm = false, nc = false;
		char m[4][4];
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				char c;
				do {
					cin >> c;
				}while(!(c == 'X' || c == 'T' || c == 'O' || c == '.'));
				m[i][j] = c;
			}
		}
		int xc3 = 0, oc3 = 0, tc3 = 0, dc3 = 0, dc1 = 0, dc2 = 0;
		int xc4 = 0, oc4 = 0, tc4 = 0, dc4 = 0;

		for(int i = 0; i < 4; i++){
			int xc1 = 0, oc1 = 0, tc1 = 0, ldc1 = 0;
			int xc2 = 0, oc2 = 0, tc2 = 0, ldc2 = 0;
			for(int j = 0; j < 4; j++){
				switch(m[i][j]){
					case 'X':
						xc1++;
						break;
					case 'O':
						oc1++;
						break;
					case 'T':
						tc1++;
						break;
					case '.':
						ldc1++;
						break;
				}
				switch(m[j][i]){
					case 'X':
						xc2++;
						break;
					case 'O':
						oc2++;
						break;
					case 'T':
						tc2++;
						break;
					case '.':
						ldc2++;
						break;
				}
				if(i == j){
					switch(m[i][j]){
						case 'X':
							xc3++;
							break;
						case 'O':
							oc3++;
							break;
						case 'T':
							tc3++;
							break;
						case '.':
							dc3++;
							break;
					}
				}
				if(i+j == 3){
					switch(m[j][i]){
						case 'X':
							xc4++;
							break;
						case 'O':
							oc4++;
							break;
						case 'T':
							tc4++;
							break;
						case '.':
							dc4++;
							break;
					}

				}
			}
			if(ldc1)
				dc1 = ldc1;
			if(ldc2)
				dc2 = ldc2;

			if(xc1 == 4 || (xc1 == 3 && tc1 == 1))
				xw = true;
			if(oc1 == 4 || (oc1 == 3 && tc1 == 1))
				ow = true;
			if(xc2 == 4 || (xc2 == 3 && tc2 == 1))
				xw = true;
			if(oc2 == 4 || (oc2 == 3 && oc2 == 1))
				ow = true;

		}

		if(xc3 == 4 || (xc3 == 3 && tc3 == 1))
			xw = true;
		if(oc3 == 4 || (oc3 == 3 && tc3 == 1))
			ow = true;
		if(xc4 == 4 || (xc4 == 3 && tc4 == 1))
			xw = true;
		if(oc4 == 4 || (oc4 == 3 && tc4 == 1))
			ow = true;

		if(!xw && !ow){
			if(dc1 || dc2 || dc3){
				nc = true;
			}
			else {
				dm = true;
			}
		}

		if(xw){
			cout << "Case #" << ++t << ": " << "X won" << endl;
		}
		else if(ow){
			cout << "Case #" << ++t << ": " << "O won" << endl;
		}
		else if(nc){
			cout << "Case #" << ++t << ": " << "Game has not completed" << endl;
		}
		else {
			cout << "Case #" << ++t << ": " << "Draw" << endl;
		}
	}
	return 0;
}
