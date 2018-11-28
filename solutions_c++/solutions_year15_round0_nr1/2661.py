#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <queue>


using namespace std;



void gcj_solve(int caseno, ifstream &in, ofstream &out) {
	int sm;
	string s;
	in >> sm >> s;
	int ans = 0;
	int t = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] - '0' > 0 && t < i) {
			ans += i - t;
			t = i;
		}
		t += s[i] - '0';
	}
	out << "Case #" << caseno << ": " << ans << "\n";
}

int google_code_jam() {
	ifstream in("input.in");
	ofstream out("output.out");
	if (!in.is_open() || in.eof() || !out.is_open()) {
		cout << "error" << endl;
		return -1;
	}
	int nc;
	in >> nc;
	for (int i = 1; i <= nc; i++) {
		if (in.eof()) {
			cout << "error 2" << endl;
			return -1;
		}
		gcj_solve(i, in, out);
	}
	in.close();
	out.close();
	return 0;
}

int main() {
	google_code_jam();
}