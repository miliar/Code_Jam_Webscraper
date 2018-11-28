#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
#include <vector>

using namespace std;

static int Isqrt(int num) {
	if(0 == num) return 0;
	int n = (num/2) + 1;
	int n1 = (n+(num/n))/2;
	while(n1 < n) {
		n = n1;
		n1 = (n+(num/n))/2;
	}
	return n;
}

static bool IsPalindrome(int num) {
	vector<int> vec;
	int quo = num;
	while(quo > 0) {
		vec.push_back(quo%10);
		quo = quo/10;
	}
	int vsize = vec.size();
	for(int i=0; i<vsize/2; i++) {
		if(vec[i] != vec[vsize - 1 - i]) return false;
	}
	return true;
}

static bool IsSquareNPalindrome(int num) {
	if(Isqrt(num) * Isqrt(num) == num) {
		return IsPalindrome(Isqrt(num));
	}
	return false;
}

int checkSquareNPalindrome(int m, int n) {
	int count = 0;
	for(int i=m; i<=n; i++) {
		if(IsPalindrome(i)) {
			if(IsSquareNPalindrome(i)) {
				count += 1;
			}
		}
	}
	return count;
}

int main() {
	string line;
	ifstream infile;
	ofstream outfile;
	int m,n;
	int result;
	infile.open("input.txt");
	outfile.open("output.txt");
	getline(infile, line);  // read test case number#
	int nCase = atoi(line.c_str());
	for(int i=0; i<nCase; i++) {
		getline(infile, line);
		istringstream is(line);
		is >> m;
		is >> n;
		result = checkSquareNPalindrome(m, n);
		outfile << "Case #" << i+1 << ": ";
		outfile << result << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
