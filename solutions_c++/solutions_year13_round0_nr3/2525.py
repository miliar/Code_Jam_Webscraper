#include <cmath>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int64_t T;
int64_t A, B;
vector<int64_t> v;

int64_t sqrtc(int64_t n) {
	return ceil(sqrt(n));
}
int64_t sqrtf(int64_t n) {
	return floor(sqrt(n));
}
template<typename T>
string to_s(T n) {
	ostringstream os;
	os << n;
  return os.str();
}
bool fair(int64_t n) {
	string s = to_s(n);
	return equal(s.begin(), s.end(), s.rbegin());
}

void prep() {
	int64_t i;
//	A=1;B=1000;
	A=1;B=100000000000000;
	int64_t b=sqrtc(A);
	int64_t e=sqrtf(B);
	//int64_t count=0;
	for (i=b;i<=e;i++) {
		if (fair(i)) {
			int64_t sq = i*i;
			if (fair(sq)) {
				v.push_back(sq);
	//			cout << sq << endl;
	//			count++;
			}
		}
	}
	//return count;
}

int64_t solve() {
	return upper_bound(v.begin(), v.end(), B) - lower_bound(v.begin(), v.end(), A);
}

int main() {
	prep();
	cin >> T;
	for (int64_t i=1; i<=T; i++) {
		cin >> A >> B;
	  cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
