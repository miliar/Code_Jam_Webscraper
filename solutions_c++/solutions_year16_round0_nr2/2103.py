#include <iostream>
#include <fstream>
#include <string>

#define REP(i, a, b)		for(i = (int)a; i<=(int)b ; i++)
#define FOR(i, N)			REP(i, 0, N-1)

using namespace std;

int main(){
	ifstream cin("B.in");
	ofstream cout("B-Large.out");

	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i;
		string str;
		cin >> str;

		int ans = 0;
		char c = str[0];
		FOR(i, str.size()) if (str[i] != c) {
			c = str[i];
			ans++;
		}
		if (str.back() == '-')
			ans++;

		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}