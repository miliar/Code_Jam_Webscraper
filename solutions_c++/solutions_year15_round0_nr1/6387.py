#include <iostream>
#include <string>
#include <vector>

#define FIN(s, n) for (const auto & s : n)
#define FOR(i, n) for (UI i = 0; i < n; ++i)
#define UP(min, n) min = (n > min) ? n : min

using namespace std;

typedef unsigned int UI;
typedef vector<UI> VUI;


UI T, smax;
VUI shyness;

void input() {
	string str_shyness;
	cin >> smax;
	cin >> str_shyness;

	FIN(s, str_shyness) {
		shyness.push_back((UI) s - '0');
	}
}

int main() {
	cin >> T;
	FOR(i, T) {
		input();
		UI minadd = 0;
		UI total = 0;
		FOR (i, shyness.size()) {
			if (i > total) {
				total -= minadd;
				UP(minadd, i - total);
				total += minadd;
			}
			total += shyness[i];
		}

		cout << "Case #" << i+1 << ": " << minadd << endl;
		shyness.clear();
	}

	return 0;
}
