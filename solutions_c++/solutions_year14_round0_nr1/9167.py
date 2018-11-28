#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream inData("input.txt");
	ofstream outData("output.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++){
		int first;
		inData >> first;
		int a1[4][4];
		for(int k=0; k < 4; k++){
			for(int j=0; j < 4; j++){
				int temp;
				inData >> temp;
				a1[k][j] = temp;
			}
		}

		int second;
		inData >> second;
		int a2[4][4];
		for(int k=0; k < 4; k++){
			for(int j=0; j < 4; j++){
				int temp;
				inData >> temp;
				a2[k][j] = temp;
			}
		}

		int output = 0;
		for(int k=0; k < 4; k++){
			for(int j=0; j < 4; j++){
				if(a1[first-1][k] == a2[second-1][j]){
					if(output == 0){
						output = a1[first-1][k];
					}
					else{
						output = -1;
					}
				}
			}
		}

		if(output == 0){
			outData << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		}
		else if(output == -1){
			outData << "Case #" << i+1 << ": Bad magician!" << endl;
		}
		else {
			outData << "Case #" << i+1 << ": " << output<< endl;
		}
	}

	return 0;
}