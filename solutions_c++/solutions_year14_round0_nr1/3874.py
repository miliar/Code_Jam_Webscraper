#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string filein = "A-small-attempt0.in", fileout = "output.txt";
const unsigned int H = 4, W = 4;

typedef unsigned int arr[H][W];
typedef unsigned int arrRow[W];
typedef enum tResult {found, bad_magician, volunteer_cheated};

void print(ofstream &fo, unsigned int i, tResult res, unsigned int n);
bool magicTrick(string fin, string fout);
bool loadArr(ifstream &fi, arr &arr);
tResult testArr(arr &arr1, arr &arr2, unsigned int c1, unsigned int c2, unsigned int &n);
void pause();

int main() {
	if (magicTrick(filein, fileout)) cout << "There were errors." << endl;
	else cout << "There were no errors. Output is saved in: " << fileout << "." << endl;
	pause();
	return 0;
}

bool magicTrick(string fin, string fout) {
	bool error = false;
	ifstream fi;
	fi.open(fin);
	ofstream fo;
	fo.open(fout);
	if (!fi.is_open() || !fo.is_open()) {
		cout << "Error opening file(s).";
		return true;
	} else {
		unsigned int cases;
		fi >> cases;
		for (unsigned int i = 1; i <= cases && !error; i++) {
			unsigned int c1, c2;
			fi >> c1;
			arr arr1;
			bool error = loadArr(fi, arr1);
			if (!error) {
				fi >> c2;
				arr arr2;
				bool error = loadArr(fi, arr2);
				if (!error) {
					unsigned int n; c1--; c2--;
					tResult res = testArr(arr1, arr2, c1, c2, n);
					print(fo, i, res, n);
				}
			} 
		}
		fo.close(); fi.close();
		return error;
	}
}

void pause() {
	cin.clear();
	cin.sync();
	cout << "Press Intro to continue...";
	cin.ignore(INT_MAX, '\n');
}

void print(ofstream &fo, unsigned int i, tResult res, unsigned int n) {
	fo << "Case #" << i << ": ";
	if (res == found) fo << n;
	else if (res == volunteer_cheated) fo << "Volunteer cheated!";
	else fo << "Bad magician!";
	fo << endl;
}

bool loadArr(ifstream &fi, arr &arr) {
	for (unsigned int i = 0; i < H && !fi.fail(); i++) {
		for (unsigned int j = 0; j < W && !fi.fail(); j++) {
			fi >> arr[i][j];
		}
	}
	if (fi.fail()) return true; else return false;
}

tResult testArr(arr &arr1, arr &arr2, unsigned int c1, unsigned int c2, unsigned int &n) {
	arrRow row;
	for (unsigned int i = 0; i < W; i++) row[i] = 0;

	for (unsigned int j = 0; j < W; j++) {
		unsigned int value = arr1[c1][j];
		bool found = false;
		for (unsigned int k = 0; k < W && !found; k++) {
			if (arr2[c2][k] == value) {
				found = true;
				row[j]++;
			}
		}
	}

	unsigned int sum = 0;
	for (unsigned int i = 0; i < W; i++) {
		sum += row[i];
	}

	if (sum == 1) {
		bool ex = false;
		for (unsigned int i = 0; i < W && !ex; i++) {
			if (row[i] == 1) {
				n = arr1[c1][i];
				ex = true;
			}
		}
		return found;
	} else if (sum == 0) return volunteer_cheated;
	else return bad_magician;
}