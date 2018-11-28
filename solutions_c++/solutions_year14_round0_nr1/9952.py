#include <iostream>
#include <fstream>

using namespace std;

bool equal(int arr1[][4], int arr2[][4], int n) {
	bool result = true;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(arr1[i][j] != arr2[i][j]) {
				result = false;
				break;
			}
		}
	}
	return result;
}

int getIndex(int arr[], int n, int key) {
	int index = -1;
	for(int i=0; i<n; i++) {
		if(key == arr[i]) {
			index = i;
			break;
		}
	}
	return index;
}

int main() {
	ifstream fin;
	//fin.open("input.txt");
	fin.open("A-small-attempt4.in");
	ofstream fout;
	fout.open("output.txt");
	
	int arr1[4][4], arr2[4][4];
	int n, first, second, i = 0;
	fin >> n;
	while(i < n) {
		fin >> first;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				fin >> arr1[j][k];
			}
		}

		fin >> second;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				fin >> arr2[j][k];
			}
		}

		int number = 0, count = 0;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				if(arr1[first-1][j] == arr2[second-1][k]) {
					number = arr1[first-1][j];
					count++;
				}
			}
		}
		if(count == 0) {
			fout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		}
		else if(count == 1) {
			fout << "Case #" << i+1 << ": " << number << endl;
		}
		else {
			fout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}
		i++;
	}

	fin.close();
	fout.close();
	return 0;
}