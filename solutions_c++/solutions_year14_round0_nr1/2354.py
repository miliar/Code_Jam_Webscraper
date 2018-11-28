#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
#define ll long long
#define inf 1000000000
#define L(s) ((int)(s).size())
#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define x first
#define y second
#define all(s) (s).begin(), (s).end()
#define mp make_pair
int tc;
int cand[16];
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tc;
	for(int tn = 1; tn <= tc; ++tn) {
		memset(cand, 0, sizeof(cand));
		int r1; cin >> r1; --r1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j) {
				int x; cin >> x; --x;
				cand[x] += (i == r1);
			}

		cin >> r1; --r1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j) {
				int x; cin >> x; --x;
				cand[x] += (i == r1);
			}
		cout << "Case #" << tn << ": ";
		if (*max_element(cand, cand + 16) < 2) {
			cout << "Volunteer cheated!\n";
		} else
			if (count(cand, cand + 16, 2) > 1) {
				cout << "Bad magician!\n";
			} else {
				cout << (max_element(cand, cand + 16) - cand) + 1 << endl;
			}
	}
}