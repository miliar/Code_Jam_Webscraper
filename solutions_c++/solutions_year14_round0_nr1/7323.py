#include <iostream>
#include <stdio.h>

using namespace std;

int grid1[4][4];
int grid2[4][4];

int main(){
	freopen("in","r",stdin);
    freopen("out","w",stdout);
	int T, guess1, guess2;
	cin >> T;
	int possible_value[17];
	int ok_value, the_value;
	for (int t=1; t<=T; t++) {
		for (int i=0; i<17; i++) possible_value[i] = 0;
		cin >> guess1;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) {
			cin >> grid1[i][j];
		}
		cin >> guess2;
		for (int i=0; i<4; i++) for (int j=0; j<4; j++) {
			cin >> grid2[i][j];
		}
		for (int i=0; i<4; i++) {
			possible_value[grid1[guess1-1][i]]++;
			possible_value[grid2[guess2-1][i]]++;
		}
		ok_value = 0;
		for (int i=1; i<=16; i++) {
			if (possible_value[i] == 2) {
				ok_value++;
				the_value = i;
			} 
		}
		printf("Case #%d: ", t);
		if (ok_value == 1) {
			printf("%d\n", the_value);
		}else if (ok_value > 1) {
			printf("Bad magician!\n");
		}else {
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}