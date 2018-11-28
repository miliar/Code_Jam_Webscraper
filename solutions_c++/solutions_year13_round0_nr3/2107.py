#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>
#include <memory.h>
using namespace std;

#define all(a) a.begin(),a.end()

template<class T, class U> T cast (U x) { ostringstream os; os<<x; T res; istringstream is(os.str()); is>>res; return res; }

bool isPalindrome(long long x) {
	string s = cast<string>(x);
	string rs = s;
	reverse(all(rs));
	return s == rs;
}

int main( int argc, char* argv[] ) {
	string path = "D:/C-large-1";
	freopen((path + ".in").c_str(), "r", stdin);
	freopen((path + ".out").c_str(), "w", stdout);
	
	vector<long long> points;
	for(long long i = 1; i <= 10000000; i++) {
		if (isPalindrome(i) && isPalindrome(i * i)) {
			points.push_back(i * i);
		}
	}

	int testCases;
	cin >> testCases;

	for(int testCase=1; testCase <= testCases; testCase++){
		long long a, b;
		cin >> a >> b;

		int res = upper_bound(all(points), b) - lower_bound(all(points), a);
		cout << "Case #" << testCase << ": " << res << endl;
		cout.flush();
	}

	fclose(stdout);
	return 0;
}
