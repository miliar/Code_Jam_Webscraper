#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>
#include <valarray>
#include <cmath>
#include <climits>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
// #define cpp11
#ifdef cpp11
	#include <unordered_map>
	#include <unordered_set>
	#include <regex>
	#include <tuple>
	#include <cstdint>
#endif

using namespace std;

//#define DO_DEBUG 1

#define INFIN 0x3f3f3f3f
#define cin fin
#define cout fout

int T;
ofstream fout ("a.out");
ifstream fin ("A-small-attempt0.in");

int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int a1, a2, answer, nans = 0;
		cin >> a1;
		int cards[17] = {0};
		for (int r = 1; r <= 4; r++) {
			for (int c = 1; c <= 4; c++) {
				int card;
				cin >> card;
				if (r == a1) {
					cards[card]++;
				}
			}
		}
		cin >> a2;
		for (int r = 1; r <= 4; r++) {
			for (int c = 1; c <= 4; c++) {
				int card;
				cin >> card;
				if (r == a2 && cards[card]) {
					nans++;
					answer = card;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if (nans == 0) cout << "Volunteer cheated!\n";
		else if (nans == 1) cout << answer << '\n';
		else cout << "Bad magician!\n";
	}
	return 0;
}