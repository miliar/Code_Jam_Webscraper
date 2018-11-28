#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;


int dat[17];

int main() {
	int round, num, cnt, i, j, k, res;
	int tmp1, tmp2, tmp3, tmp4;
	int row1, row2;
	
	
	cin>>round;
	for (i = 1; i <= round; i++) {
	
		res = 0;
		for (j = 1; j <17; j++) {
			dat[j] = 0;
		}
		
		cin>>row1;
		for (j = 1; j <= 4; j++) {
			if (j == row1) {
				for (k = 0; k < 4; k++) {
					cin>>num;
					dat[num]++;
				}
			}
			else {
				for (k = 0; k < 4; k++) {
					cin>>num;
				}
			}
		}
		cin>>row2;
		
		for (j = 1; j <= 4; j++) {
			if (j == row2) {
				for (k = 0; k < 4; k++) {
					cin>>num;
					dat[num]++;
				}
			}
			else {
				for (k = 0; k < 4; k++) {
					cin>>num;
				}
			}
		}
		
		for (j = 1; j < 17; j++) {
			if (dat[j] > 1) {
				if (res == 0) {
					res = j;
				}
				else {
					res = -1;
				}
			}
		}
		
		cout<<"Case #"<<i<<": ";
		if (res > 0) {
			cout<<res<<endl;
		
		}
		else if (res == 0) {
			cout<<"Volunteer cheated!\n";
		}
		else {
			cout<<"Bad magician!\n";
		}
	}
	return 0;
}

