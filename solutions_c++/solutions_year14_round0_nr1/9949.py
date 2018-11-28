#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	int test;
	cin >> test;
	int A[4][4] = {0},B[4][4] = {0};
	int ans = 0;

	for(int x = 1; x <= test; x++){
		
		int count = 0, row1, row2;

		cin >> row1;	
		for(int i = 0; i < 4 ; i++){
			for(int j = 0; j < 4; j++){
				cin >> A[i][j];
			}
		}

		cin >> row2;
		for(int i = 0; i < 4 ; i++){
			for(int j = 0; j < 4; j++){
				cin >> B[i][j];
			}
		}

		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4 ; ++j){
				if(A[row1-1][i] == B[row2-1][j]){
					count++;
					ans = A[row1-1][i];
				}
			}
		}
		if(count == 0){
			cout << "Case #" << x << ": Volunteer cheated!\n";
		}else if(count == 1){
			cout << "Case #" << x << ": " << ans << "\n";			
		}else{
			cout << "Case #" << x << ": Bad magician!\n";
		}
	}
	return 0;
}
