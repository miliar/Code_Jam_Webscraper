#include<iostream>
#include<fstream>
using namespace std;


int arr[10000];
int numParties;
bool allZero() {
	for (int i = 1; i <= numParties; i++) {
		if (arr[i] != 0) {
			return false;
		}
	}
	return true;
}
int main() {
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	for (int q = 1; q <= t; q++) {
		fin >> numParties;
		for (int i = 1; i <= numParties; i++) {
			fin >> arr[i];
		}
		fout << "Case #" << q << ": ";
		for (int j = 0; !allZero(); j++) {
			int maxI = 1, max = 0;
			for (int i = 1; i <= numParties; i++) {
				if (arr[i] > max) {
					max = arr[i];
					maxI = i;
				}
			}
			/*int max2 = 0;
			for (int i = 1; i <= numParties; i++) {
				if (arr[i] > max2 && arr[i] < max) {
					max2 = arr[i];
				}
			}
			if (max - max2 == 2) {

			}*/
			arr[maxI] = arr[maxI] - 1;
			int maxI2 = 1;
			bool flag = false;
			for (int k = 1; k <= numParties; k++) {
				if (max == arr[k] && k!=maxI) {
					maxI2 = k;
					flag = true;
					break;
				}
			}
			bool flag1 = false;
			for (int i = maxI2+1; i <= numParties; i++) {
				if (arr[i] == max) {
					flag1 = true;
					break;
				}
			}
			char c1, c2;
			c1 = maxI + 64;
			//c2 = maxI2 + 64;
			if (flag1) {
				fout << c1 << " ";
				continue;
			}
			if (flag) {
				arr[maxI2] = arr[maxI2] - 1;
			}
			c1 = maxI + 64;
			c2 = maxI2 + 64;
			if (flag) {
				fout << c1 << c2 << " ";
			}
			else {
				fout << c1 << " ";
			}
		}
		fout << endl;

	}
	return 0;
}