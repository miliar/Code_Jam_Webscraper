#include <iostream>
#include <string>

using namespace std;

int main(){
	int numCases;
	int currentCase = 0;
	cin >> numCases;
	//int arr[4][4] arr1, arr2;
	int row1, row2;
	int rowarr1[4], rowarr2[4];
	int junk;
	while(currentCase++ < numCases){
		cin >> row1;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				if(i == row1 - 1){
					cin >> rowarr1[j];
				}
				else cin >> junk;
			}
		}
		cin >> row2;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				if(i == row2 -1){
					cin >> rowarr2[j];
				}
				else cin >> junk;
			}
		}

		for(int i = 0; i < 4; ++i){
			cerr << rowarr1[i] << " " << rowarr2[i] << endl;
		}

		int intersect = -1;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				if(rowarr1[i] == rowarr2[j]){
					if(intersect == -1){
						intersect = rowarr1[i];
					}
					else intersect = -2;
				}
			}
		}

		cout << "Case #" << currentCase << ": ";
		if(intersect == -1){
			cout << "Volunteer cheated!" << endl;
		}
		else if(intersect == -2){
			cout << "Bad magician!" << endl;
		}
		else {
			cout << intersect << endl;
		}

	}
}