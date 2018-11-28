#include <iostream>
using namespace std;

int main(){
	int T, arr[2][16], row[2];
	cin >> T;
	for(int k=1;k<=T;k++){
		int b = 0;
		cout << "Case #" << k << ": ";
		int count = 0;
		for (int i=0;i<2;i++){
			cin >> row[i];
			for (int j=0;j<16;j++){
				cin >> arr[i][j];
			}
		}
		for (int i=4*(row[0]-1);i<4*(row[0]);i++){
			for (int j=4*(row[1]-1);j<4*(row[1]);j++){
				if (arr[0][i] == arr[1][j]){
					if (count > 0){
						cout << "Bad magician!\n";
						i=99;
						b=1;
						break;
					} else {
						count = arr[0][i];
					}
				}
			}
		}
		if (b){
			continue;
		} else if (!count){
			cout << "Volunteer cheated!\n";
		} else {
			cout << count << endl;
		}
	}
}
