#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

char ss[] = {'P', 'R', 'S'};
int n;
int a[3];
int b[3];

string run(int x, int w) {
	string ans;
	if (x == n) {
		++b[w];
		ans += ss[w];
		return ans;
	}
	int a = w;
	int b = (w + 1) % 3;
	string al = run(x + 1, a);
	string ar = run(x + 1, b);
	if (al > ar)
		swap(al, ar);
	return al + ar;
}


string solve() {
	cin >> n >> a[1] >> a[0] >> a[2];
	string s = "Z";
	for (int i = 0; i < 3; ++i) {
		b[0] = b[1] = b[2] = 0;
		string sg = run(0, i);
		if (b[0] == a[0] && b[1] == a[1] && b[2] == a[2]) {
			s = min(s, sg);
		}
	}
	if (s == "Z")
		return "IMPOSSIBLE";
	else
		return s;
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		string s = solve();
		cout << "Case #" << i + 1 << ": " << s << "\n";
	}
	return 0;
}


