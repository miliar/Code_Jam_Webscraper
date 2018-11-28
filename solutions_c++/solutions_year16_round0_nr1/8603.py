#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int tt, nr;
int tab[10];

void rob(int x) {
	while(x > 0) {
		tab[x % 10] = 1;
		x /= 10;
	}
}

void czysc() {
	for(int i = 0; i < 10; ++i) tab[i] = 0;
}

bool jest() {
	for(int i = 0; i < 10; ++i) if(!tab[i]) return 0;
	return 1;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin >> tt;
	nr = 1;
	while(nr <= tt) {
		int n;
		cin >> n;
		if(n == 0) cout << "Case #" << nr << ": INSOMNIA\n";
		else {
			int m = n;
			czysc();
			while(1) {
				rob(n);
				if(jest()) break;
				n += m;
			}
			cout << "Case #" << nr << ": " << n << endl;
		}
		nr++;
	}
	//system("pause");
	return 0;
}