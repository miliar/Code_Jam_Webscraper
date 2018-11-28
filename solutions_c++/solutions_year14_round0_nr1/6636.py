#include <iostream>

using namespace std;

int first_row[5];
int second_row[5];

int main(){
	int T, i, j, k, row, aux, rep, elem;
	cin >> T;
	for(i = 1; i <= T; ++i){
		cin >> row;
		for(j = 1; j <= 4; ++j){
			for(k = 1; k <= 4; ++k){
				cin >> aux;
				if(j == row){
					first_row[k] = aux;
				}
			}
		}
		cin >> row;
		for(j = 1; j <= 4; ++j){
			for(k = 1; k <= 4; ++k){
				cin >> aux;
				if(j == row){
					second_row[k] = aux;
				}
			}
		}
		rep = 0;
		for(j = 1;j <= 4;++j){
			for(k = 1;k <= 4;++k){
				if(first_row[j] == second_row[k]){
					rep++;
					elem = first_row[j];
					break;
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(rep == 1){
			cout << elem;
		}else if(rep > 1){
			cout << "Bad magician!";
		}else{
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}
	
	return 0;
}

