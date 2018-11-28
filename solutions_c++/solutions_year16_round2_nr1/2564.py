#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define REP(i, a, b)		for(i = (int)a; i<=(int)b ; i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define All(v)				v.begin(), v.end()

#define VI					vector<int>
#define VS

using namespace std;

VI Letters;
VI num;

int main() {
	ifstream cin("A.in");
	ofstream cout("A-Large.out");

	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i, j;
		string str;
		cin >> str;

		Letters = VI(26, 0);
		FOR(i, str.size())
			Letters[str[i] - 'A']++;

		num = VI(10, 0);
		num[0] = Letters['Z' - 'A'];
		num[2] = Letters['W' - 'A'];
		num[4] = Letters['U' - 'A'];
		num[6] = Letters['X' - 'A'];
		num[8] = Letters['G' - 'A'];
		num[1] = Letters['O' - 'A'] - num[0] - num[2] - num[4];
		num[3] = Letters['H' - 'A'] - num[8];
		num[7] = Letters['S' - 'A'] - num[6];
		num[5] = Letters['V' - 'A'] - num[7];
		num[9] = Letters['I' - 'A'] - num[5] - num[6] - num[8];

		cout << "Case #" << t << ": ";
		FOR(i, 10) FOR(j, num[i])
			cout << i;
		cout << endl;
	}
	return 0;
}