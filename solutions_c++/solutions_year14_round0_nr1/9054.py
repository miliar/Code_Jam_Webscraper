using namespace std;
#include <iostream>
#include <cstdio>
#include <string>

int main(){
	int t, answer, match, res;
	int grid[4][4], possible[4];

	cin >> t;

	for(int i = 1;i <= t;i++){
		cin >> answer;
		answer--;

		match = 0;

		for(int l = 0;l < 4;l++){
			for(int j = 0;j < 4;j++){
				cin >> grid[l][j];
			}
		}
	
		for(int l = 0;l < 4;l++){
			possible[l] = grid[answer][l];
		}

		cin >> answer;
		answer--;

		for(int l = 0;l < 4;l++){
			for(int j = 0;j < 4;j++){
				cin >> grid[l][j];
			}
		}

		for(int l = 0;l < 4;l++){
			for(int j = 0;j < 4;j++){
				if(possible[l] == grid[answer][j]){
					res = possible[l];
					match++;
				}
			}
		}

		cout << "Case #" << i << ": "; 

		if(match == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else if(match == 1){
			cout << res << endl;
		}
		else{
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}
