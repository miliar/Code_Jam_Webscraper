#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

string solve()
{
	int a1, a2;
	set<int> s1;
	set<int> s2;

	cin >> a1;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int b;
			cin >> b;
			if (i == a1) { s1.insert(b); }
		}
	}

	cin >> a2;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int b;
			cin >> b;
			if (i == a2) { s2.insert(b); }
		}
	}
	set<int> s;
	set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), std::inserter(s, s.begin()));
	if (s.size() > 1) {
		return "Bad magician!";
	}
	if (s.size() == 0) {
		return "Volunteer cheated!";
	}
	stringstream ss;
	ss << *(s.begin());
	return ss.str();
}

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}

