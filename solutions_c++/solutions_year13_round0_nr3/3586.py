#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

typedef unsigned long long int integer;
//map<integer, bool> known;


int T, I;
integer A, B;
integer a, b, c, C;
int R;

void print() {
	//cout << "Case #" << (I+1) << ": " << R << endl;
	printf("Case #%d: %d\n", I, R);
}

void read() {
	//cin >> A >> B;
	scanf("%llu %llu\n", &A, &B);
}

inline integer reverse(integer i) {
	integer rev = 0;
	integer num = i;
	while (num>0) {
		rev = rev*10+(num%10);
		num = num/10;
	}
	return rev;
}

/*
inline bool palindrome(integer i) {
	if (known.find(i) == known.end()) {
		known[i] = i - reverse(i) == 0;
	}
	return known[i];
}
*/

inline bool palindrome(integer i) {
	return i - reverse(i) == 0;
}

void solve() {
	R = 0;
	a = (integer) (sqrt(A)-1);
	b = (integer) (sqrt(B)+1);
	for (c = a; c < b; c++) {
		if (palindrome(c)) {
			C = c*c;
			R += palindrome(C) && (C >= A) && (C <= B);
		}
	}
}

void main() {
	cin >> T;
	T++;
	for (I = 1; I<T; I++) {
		read();
		solve();
		print();
	}
}