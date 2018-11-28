#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <ctime>
#include <cstring>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi >
#define pii pair<int,int>
#define pll pair<ll,ll>
#define vpii vector<pii >
#define vb vector<bool>
#define min(x,y) (x < y ? x : y)
#define max(x,y) (x > y ? x : y)
#define forn(i,n) for(int i = 0;i < n;i++)
#define sqrt(x) (pow(x,0.5))
#define sqr(x) (x * x)
#define mp make_pair
#define TASKNAME ""

const int inf = 1e9;
const ll infll = 1e18;
const int mod = 1e9 + 7;
const ld eps = 1e-9;

using namespace std;


void solve() {
	int n;
	cin >> n;
	string line;
	string scl = "";
	vi charcount;
	vvi ccharcount(n);
	for (int i = 0; i < n; i++) {
		cin >> line;
		string sc = "";
		int cc = 1, cc2 = 0;
		for (int j = 0; j < line.size(); j++) {
			if (j == 0) 
				sc += line[j];
			else if (line[j] != sc.back()) {
				sc += line[j];
				if (i == 0)
					charcount.push_back(cc);
				else {
					if (cc2 >= charcount.size()){
						cout << "Fegla Won" << endl;
						return;
					}
					charcount[cc2] += cc;
				}
				ccharcount[i].push_back(cc);
				cc = 1;
				cc2++;
			}
			else cc++;
		}
		if (i == 0)
			charcount.push_back(cc);
		else {
			if (cc2 >= charcount.size()){
				cout << "Fegla Won" << endl;
				return;
			}
			charcount[cc2] += cc;
		}
		ccharcount[i].push_back(cc);
		if (i == 0)
			scl = sc;
		else if (scl != sc) {
			cout << "Fegla Won" << endl;
			return;
		}
	}
	int ans = 0;
	for (int i = 0; i < charcount.size(); i++)
		charcount[i] /= n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < charcount.size(); j++) {
			ans += abs(ccharcount[i][j] - charcount[j]);
		}
	}
	cout << ans << endl;
}

int main(int argv,char** argc) {
	freopen("INPUT.TXT","r",stdin); freopen("OUTPUT.TXT","w",stdout);
	//freopen(TASKNAME".in","r",stdin); freopen(TASKNAME".out","w",stdout);
	int tests = 0;
	cin >> tests;
	for (int i = 0; i < tests; i++) {
		cout << "Case #" << (i + 1) << ": ";

		solve();
	}

	return 0;
}