#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main() {
ifstream myfile("input.txt");
	int num;
	myfile >> num;
	int row;
	int _row;
	int req_row[4][4];
	int req_row1[4][4];
	vector<int> vec;
	int ans[4];
	
	for(int i = 0; i < num; i++) {
	int size = 0;
		myfile >> row;
		for(int k = 0; k < 4 ; k++) {
			for(int l = 0; l < 4 ; l++) {
				myfile >> req_row[k][l];
			}
		}
		myfile >> _row;
		for(int k = 0; k < 4 ; k++) {
			for(int l = 0; l < 4 ; l++) {
				myfile >> req_row1[k][l];
			}
		}
		for(int k = 0; k < 4 ; k++) {
			for(int l = 0; l < 4 ; l++) {
				if(req_row1[_row-1][k] == req_row[row-1][l]){
					ans[size] = req_row1[_row-1][k];
					size++;
				}
			}
		}
		if(size == 0) {
			cout << "Case #3: Volunteer cheated!"<< endl;
		} else if(size == 1) {
			cout << "Case #1: " << ans[0] << endl;
		} else if(size > 1) { 
			cout << "Case #2: Bad magician!"<< endl;
		}
	}

return 0;
}