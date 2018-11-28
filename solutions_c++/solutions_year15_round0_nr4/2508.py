#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

typedef long long ll;

int x, r, c;
int t;

string ans[2] = {"GABRIEL", "RICHARD"};

int main()
{
	freopen("input", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> x >> r >> c;
		int res = -1;
		if(x == 1) {
			res = 0;
		}
		else if(x == 2) {
			res = (r * c) % 2;
		}
		else if(x == 3) {
			res = (r == 1 || c == 1 || r * c % 3);
		}
		else if(x == 4) {
			if((r >= 3 && c == 4) || (r == 4 && c >= 3)) {
				res = 0;
			}
			else {
				res = 1;
			}
		}
		cout << "Case #" << (i + 1) << ": " << ans[res] << endl;
	}
	return 0;
}
