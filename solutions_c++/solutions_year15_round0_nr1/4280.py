#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;


int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, Smax;
	string S;
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		cin >> Smax >> S;
		int lev = 0, ans = 0;
		for (int i = 0; i <= Smax; i++) {
			if (lev < i) {
				ans += i - lev;
				lev = i;
			}
			lev += S[i] - '0';
		}
		cout << "Case #" << caso << ": " << ans << endl;
	}

	return 0;
}
