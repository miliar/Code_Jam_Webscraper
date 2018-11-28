#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

void solvePr2() {
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int a,b,n;
		cin >> a >> b >> n;
		int ans = 0;
		FOR(i,0,a) {
			FOR(j,0,b) {
				if((i&j) < n) {
					ans++;
				}
			}
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}

int main() {
	freopen("C:/Users/deepd/Downloads/in.txt", "r", stdin);
	freopen("C:/Users/deepd/Downloads/out.txt", "w", stdout);
	solvePr2();
	return 0;
}
