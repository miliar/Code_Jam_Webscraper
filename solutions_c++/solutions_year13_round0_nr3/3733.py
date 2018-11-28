#include <iostream>
#include <cstdio>
#include <climits>
#include <cmath>
#include <vector>

using namespace std;

bool isPalindromic(long long n) {
	char buf[101];
	sprintf(buf, "%Ld", n);
	
	int len = strlen(buf);
	for( int i = 0; i < len / 2; i++ ) {
		if ( buf[i] != buf[len-i-1] ) return false;
	}


	return true;
}

bool isFairAndSquare(long long n) {
	if (!isPalindromic(n)) return false;
	long long rt = sqrt(n);
	if ( rt * rt != n ) return false;
	if (!isPalindromic(rt)) return false;
	return true;
}

vector<int> ans;
int solve(int A, int B) {
	int n = 0;
	for(int i = 0; i < ans.size(); i++) {
		if( ans[i] >= A && ans[i] <= B ) {
			n++;
		}
	}

	return n;
}

int main() {
	int numCases;
	cin >> numCases;

	for(int i = 0; i < 1001; i++) {
		if ( isFairAndSquare(static_cast<long long>( i ) ) ) {
			ans.push_back(i);
		}
	}

	for (int c = 1; c <= numCases; c++) {
		int A, B;
		cin >> A >> B;
		cout << "Case #" << c << ": " << solve(A, B) << endl;
	}

	return 1;
}