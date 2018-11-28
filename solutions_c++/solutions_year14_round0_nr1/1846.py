#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream cout("out.ou");
	int times;
	cin >> times;
	int first, second, unused;
	int status;
	int result;
	int* firstRow = new int[4];
	for (int i = 1; i <= times; i++){
		status = -1;
		cin >> first;
		for (int j = 1; j <= 4; j++){
			if (j == first){
				cin >> firstRow[0] >> firstRow[1] >> firstRow[2] >> firstRow[3];
			}
			else{
				cin >> unused >> unused >> unused >> unused;
			}
		}

		cin >> second;
		for (int j = 1; j <= 4; j++){
			if (j == second){
				int col;
				for (int k = 0; k < 4; k++){
					cin >> col;
					for (int l = 0; l < 4; l++){
						if (firstRow[l] == col){
							status++;
							result = col;
						}
					}
				}
			}
			else{
				cin >> unused >> unused >> unused >> unused;
			}
		}

		cout << "Case #" << i << ": ";
		if (status < 0){
			cout << "Volunteer cheated!";
		}
		else if (status == 0){
			cout << result;
		}
		else{
			cout << "Bad magician!";
		}
		cout << endl;
	}
}