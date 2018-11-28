#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = 12;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		vector<string> mnP, mnR, mnS;
		mnP.push_back("P");
		mnR.push_back("R");
		mnS.push_back("S");
		for (int i = 1; i <= n; i++) {
			mnP.push_back(min(mnP[i - 1] + mnR[i - 1], mnR[i - 1] + mnP[i - 1]));
			mnR.push_back(min(mnR[i - 1] + mnS[i - 1], mnS[i - 1] + mnR[i - 1]));
			mnS.push_back(min(mnS[i - 1] + mnP[i - 1], mnP[i - 1] + mnS[i - 1]));
		}
		
		string ans = "";
		function<void(string)> f = [&](string str) {
			int cntP = 0, cntR = 0, cntS = 0;
			for (int i = 0; i < (int)str.length(); i++) {
				if (str[i] == 'P') cntP++;
				if (str[i] == 'R') cntR++;
				if (str[i] == 'S') cntS++;
				if (cntP == p && cntR == r && cntS == s && (ans == "" || ans > str)) {
					ans = str;
				}
			}
		};
		f(mnP.back());
		f(mnR.back());
		f(mnS.back());
		
		if (ans == "") ans = "IMPOSSIBLE";
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}