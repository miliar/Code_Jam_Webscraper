#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <cmath>
using namespace std;

long long sqrt2(long long x, bool upper) {
	if (0 == x) {
		return 0;	
	}
	long long low = 1, high = x/2+1;
	while (low <= high) {
		long long mid = low + (high-low) / 2;
		if (mid > numeric_limits<long long>::max() / mid || mid*mid > x) {
			high = mid-1;	
		}else if (mid*mid < x) {
			low = mid+1;	
		}else if (mid*mid == x) {
			return mid;	
		}
	}
	if (upper) {
		return low;	
	}else {
		return low-1;
	}
}

bool isPalindrome(long long  x) {	
	long long y = x, d = 1;
	while (y > 9) {
		d *= 10;
		y /= 10;
	}				
	y = x;
	while (y > 0) {
		if (y/d != y%10) {
			return false;	
		}
		y %= d;
		y /= 10;
		d /= 100;
	}
	return true;		
}

int func(long long A, long long B) {
	long long res = 0;	
	long long rA = sqrt2(A, true);
	long long rB = sqrt2(B, false);		
	for (long long r = rA; r <= rB; r++) {
		long long c = r*r;
		if (isPalindrome(c) && isPalindrome(r)) {
			res++;	
		}
	}
	return res;	
}

void solve() {
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	int T = 0;
	in >> T;
	for (int t = 1; t <= T; t++) {
		long long A, B;
		in >> A;
		in >> B;
		int res = func(A, B);
		out << "Case #" << t << ": " << res << endl;
	}
	in.close();
	out.close();
}

int main() {
	solve();	
	return 0;	
}
