/*
  Google Code Jam 2013
  Problem C
  Coded by Michael Oliver
*/
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<string> vs;

bool is_palindrome(int n) {
	if (n / 10 == 0) return true;
	else {
		int last = n % 10;
		int first = n / 10;
		int middle = 0;
		while (first >= 10) {
			middle *= 10;
			middle += first % 10;
			first /= 10;
		}
		if (first == last) return is_palindrome(middle);
		else return false;
	}
}

int is_psquare(int n) {
	ld d_sqrt = sqrt(n);
	ll i_sqrt = d_sqrt;
	if ( d_sqrt == i_sqrt ) return i_sqrt;
	else return 0;
}

int main() {
	int num_cases;
	cin >> num_cases;
	for (int i=1; i <= num_cases; i++) {
		int a, b, count = 0;
		cin >> a >> b;
		for (int j=a; j <= b; j++) {
			int test = is_psquare(j);
			if (test && is_palindrome(test) && is_palindrome(j)) count++;
		}
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
