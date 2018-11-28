//#include"stdafx.h"
#include<iostream>

using namespace std;

int main()
{
	int t, a[2], mat[2][4][4], count, ax, ay;
	cin >> t;
	for (int i = 1; i <= t; i++){
		for (int m = 0; m<2; m++){
			cin >> a[m];
			for (int x = 0; x<4; x++){
				for (int y = 0; y<4; y++){
					cin >> mat[m][x][y];
				}
			}
		}
		count = 0; ax = 0; ay = 0;
		for (int x = 0; x<4; x++){
			for (int y = 0; y<4; y++){
				if (mat[0][a[0] - 1][x] == mat[1][a[1] - 1][y]){
					if (count == 0){
						ax = a[0]-1; ay = x;
					}
					count++;
				}
			}
		}
		if (count == 1){
			cout << "Case #" << i << ": " << mat[0][ax][ay] << endl;
		}
		else if (count == 0){
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else{
			cout << "Case #" << i << ": Bad magician!" << endl;
		}
	}
	return 0;
}