#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

typedef long long tl; //type long
int _tc;

bool testCase() {
	std::string ss;
	cin >> ss;

	std::string a;
	for (int i = 0; i < ss.size(); ++i) {
		if (a.size() == 0 || ss[i] >= a[0]) {
			a.insert(0, 1, ss[i]);
		}
		else {
			a += (ss[i]);
		}
	}
	cout << a;
	return true;
}

int main(){
	int ntc;

	cin >> ntc;
	//cerr << "tests " << n << endl;
	for (int _tc = 0; _tc < ntc; ++_tc) {
		cout << "Case #" << (_tc + 1) << ": ";
		if (!testCase()) {
			cout << " IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}