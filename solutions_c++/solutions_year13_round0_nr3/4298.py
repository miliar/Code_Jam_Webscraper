#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool check_palindrome(const long long& n) {
	long long n_1 = n, rev = 0;
	while(n_1 > 0) {
		rev = rev * 10 + n_1 % 10;
		n_1 /= 10;
	}
	return n == rev;
}

long count_fs(const long double& a, const long double& b) {
	long double a_n = ceil(sqrt(a));
	long double b_n = floor(sqrt(b));
	long count = 0;
	for(long long i = a_n; i <= b_n; ++i)
		if(check_palindrome(i) && check_palindrome(i*i)) ++count;
	return count;
}

int main() {
	ifstream fin ("fairsquare.in");
	ofstream fout ("fairsquare.out");

	int n;
	fin >> n;

	for(int i = 0; i < n; ++i) {
		long double a, b;
		fin >> a >> b;
		fout << "Case #" << (i+1) << ": " << count_fs(a, b) << "\n";
	}
	fout << endl;

	return 0;
}