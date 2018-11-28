#include<iostream>
#include<sstream>
#include<cmath>
#include<fstream>
using namespace std;

bool isPalindrom(float x) {
	if(x - (int)x > 0)
		return false;
	x = (int) x;
	string st;
	stringstream ss;
	ss << x;
	ss >> st;
	int size = st.size();
	for (int i = 0; i < size / 2; ++i)
		if (st[i] != st[size - i - 1])
			return false;
	return true;
}

bool isFairAndSq(int x) {
	if (isPalindrom(x) && isPalindrom(sqrt(x))){
		return true;
	}
	return false;
}

int findInRange(int x, int y) {
	int count = 0;
	for (int i = x; i <= y; ++i)
		if (isFairAndSq(i)){
			count++;
		}
	return count;
}
int main() {
	fstream fin, fout;
	fin.open("C-small-attempt0.in", ios::in);
	fout.open("C-small-attempt0.out", ios::out);
	int nOfCases, x = 0, a, b;
	fin >> nOfCases;
	while (x < nOfCases) {
		fout << "Case #" << ++x << ": ";
		fin >> a >> b;
		fout << findInRange(a, b) <<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
