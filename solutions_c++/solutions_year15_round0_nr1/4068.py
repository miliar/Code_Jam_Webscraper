#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> vi_;

int solve(const vi_& people) {
	int stand = 0, need = 0;
	for (int i = 0; i < people.size(); ++i) {
		if (stand < i) {
			need += (i - stand);
			stand += (i - stand);
		}
		stand += people[i];
	}
	return need;
}

int main() {
	int t; cin >> t;
	for (int tloop = 0; tloop < t; ++tloop) {
		int s; cin >> s;
		vi_ people(s + 1);
		string str; cin >> str;
		for (int i = 0; i <= s; ++i) people[i] = str[i] - '0';
		cout << "Case #" << tloop + 1 << ": " << solve(people) << endl;
	}
}