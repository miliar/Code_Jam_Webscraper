//Code Jam problem "Coin Jam" Qualification Round 2016
//https://code.google.com/codejam/contest/6254486/dashboard
//-Thomas Steinke codejam@thomas-steinke.net 2016-04-08

#include <iostream>
#include <string>
#include <cassert>
#include <fstream>
using namespace std;

typedef long long integer;

integer factor(integer n) {
	assert(n>1);
	for (integer i = 2; i*i <= n; i++) {
		if (n % i == 0) return i;
	}
	return -1;
}

integer inbase(string s, integer base) {
	integer B=1, A=0;
	for (int i = s.length() - 1; i >= 0; i--) {
		if (s[i]=='1') {
			A += B;
		} else {
			assert(s[i]=='0');
		}
		B *= base;
	}
	return A;
}

integer* isjamcoin(string s) {
	integer* ans = new integer[9];
	for (integer base = 2; base <= 10; base++) {
		integer x = inbase(s,base);
		integer y = factor(x);
		if (y<0) {delete[] ans; return NULL;}
		ans[base-2]=y;
	}
	return ans;
}

void testjc(string s) {
	integer* a = isjamcoin(s);
	if (a == NULL) {
		cout << s << " is not a jamcoin" << endl;
	} else {
		cout << s << ":";
		for (int i = 0; i < 9; i++) cout << " " << a[i];
		cout << endl;
		delete[] a;
	} 
}

string randbitstr(int len) {
	assert(len >= 0);
	ifstream rand("/dev/urandom");
	string s = "";
	for (int i = 0; i < len; i++) {
		char c = rand.get();
		if ((c&1)==0) s = s + "0";
		else s = s + "1";
	}
	return s;
}

void randjamcoin(int n) {
	assert(n >= 2);
	while (true) {
		string s = "1" + randbitstr(n-2) + "1";
		integer* a = isjamcoin(s);
		if (a != NULL) {
			cout << s;
			for (int i = 0; i < 9; i++) cout << " " << a[i];
			cout << endl;
			delete[] a;
			return;
		}
	}
}

int main() {
	//testjc("100011"); testjc("101");
	//for (int i = 0; i < 10; i++) cout << randbitstr(10) << endl;
	//randjamcoin(4);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N,J; cin >> N >> J;
		for (int j = 0; j < J; j++)
			randjamcoin(N);
	}
	return 0;
}

