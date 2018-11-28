#include <iostream>
#include <fstream>
#include <bitset>
#define LL long long

using namespace std;

int main() {
	LL n, ind;
	int cs = 1, tst;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for(cin >> tst; tst--; ) {
		bitset<10> seen;
		cin >> n;
		ind = 0;
		if(n == 0)
			cout << "Case #" << cs++ << ": INSOMNIA" << '\n';
		else {
			while(seen.count() < 10) {
				++ ind;
				LL cpy = n * ind;
				while(cpy) {
					seen[cpy % 10] = 1;
					cpy /= 10;
				}
			}
			cout << "Case #" << cs++ << ": " << n * ind << '\n';
		}
	}
	return 0;
}