#include <iostream>
#include <fstream>
#include <string>

using namespace std;

static int caseNum = 1;

void initFace(const string& orig, bool face[]) {
	for (int i = 0; i< orig.length(); i++) {
		if (orig[i] == '+') face[i] = true;
		else if (orig[i] == '-') face[i] = false;
	}
	return;
}

bool checkFace(bool face[], int length) {
	bool facecheck = true;
	for (int i = 0; i < length; i++) {
		facecheck = facecheck & face[i];
	}
	return facecheck;
}

void swap(bool face[], int mark) {
	for (int i = 0; i <= mark; i++) {
		face[i] = !face[i];
	}
	for (int i = 0; i < (mark + 1) / 2; i++) {
		bool temp = face[i];
		face[i] = face[mark - i];
		face[mark - i] = temp;
	}
}

bool flip(bool (&face)[10], int times, int length, int now) {

	for (int j = now; j < length || (times == 0); j++) {
		if (times == 0) {
			if (checkFace(face, length))
				return true;
			else return false;
		}
		swap(face, j);
		if (flip(face, times-1, length, j+1)) return true;
		swap(face, j);
	}
	return false;
}

void check(const string& orig, ofstream& out) {
	string temp = orig;
	bool face[10] ;
	initFace(temp, face);
	int times = 0;
	while (flip(face, times, temp.length(),0) != true) {
		times++;
	}
	cout << "Case #" << caseNum << ": " << times << endl;
	out << "Case #" << caseNum << ": " << times << endl;
}

int main() {
	string temp;
	ifstream file("B-small-attempt1.in");
	ofstream out("B-output.out");
	int T;
	file >> temp;
	T = stoi(temp);
	if (T >= 1 && T <= 100) {
		while (T != 0) {
			file >> temp;
			if (temp.length() >= 0 && temp.length() <= 10)
				check(temp, out);
			T--;
			caseNum++;
		}
	}
	return 0;
}