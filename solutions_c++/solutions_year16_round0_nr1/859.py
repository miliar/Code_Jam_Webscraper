#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

using namespace std;

const int maxn = 1e6+1e3;

string toString(int a) {
	stringstream str;
	str << a;
	return str.str();
}

int main() {
	ios_base::sync_with_stdio(0);
	ifstream cin("All.in");
	ofstream cout("All.out");
	int t;
	cin >> t;
	for (int rep = 0; rep < t; rep++) {
		int n;
		cin >> n;
		bool seen[10];
		memset(seen, 0, sizeof(seen));
		int cur = 0;
		bool dn = false;
		cout << "CASE #" << (rep+1) << ": ";
		for (int i = 0; i < 100; i++) {
			cur += n;
			string chck = toString(cur);
			for (int k = 0; k < chck.size(); k++) {
				seen[chck[k]-'0'] = true;
			}
			bool works = true;
			for (int k = 0; k < 10; k++) {
				if (!seen[k]) {
					works = false;
					break;
				}
			}
			if (works) {
				dn = true;
				cout << cur << '\n';
				break;
			}
		}
		if (!dn) {
			cout << "INSOMNIA\n";
		}
	}
	return 0;
}

