// FairAndSquare.cc

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

bool palindrome(int n)
{
	stringstream ss("");
	ss << n;
	string ns = ss.str();

	for (int i=0; i<ns.size()/2; i++) {
		if (ns[i] != ns[ns.size()-1-i])
			return false;
	}
	return true;
}

bool squareAndPalindrome(int n)
{
	double d = sqrt(n);
	int dn = (int)d;
	int dc = ceil(d);

	return dc == dn && palindrome(dn);
}

int solve(int A, int B)
{
	int c = 0;
	for (int i=A; i<=B; i++)
		if (palindrome(i) && squareAndPalindrome(i)) {
			// cout << i << ' ';
			c++;
		}
	// cout << endl;
	return c;
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for (int i=0; i<T; i++) {
		int A, B;
		cin >> A >> B;
		cout << "Case #" << (i+1) << ": " << solve(A, B) << endl;
	}

	return 0;
}