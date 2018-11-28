#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)

void solve(int cnt) {
	cout << "Case #" << cnt << ":";
	int a, b, c;
	cin >> a >> b >> c;
	FOR(i, 1, c)
		cout << " " << i;
	cout << endl;
}

int main() {
	int n;
	cin >> n;
	FOR(i, 1, n)
		solve(i);
}