#include <iostream>
#include <cstdio>

using namespace std;

typedef unsigned long long ull;

void print_binary(ull num) {
	if (num != 0) {
	print_binary(num>>1);
	printf(num%2==0 ? "0" : "1");
	}
}

ull getbasek(ull num, int k) {
	if (num == 0) return 0;
	return (num&1) + k*getbasek(num>>1, k);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("/Users/malzantot/Documents/codingspace/input.txt", "r", stdin);
	freopen("/Users/malzantot/Documents/codingspace/c-small.txt", "w", stdout);
#endif
	

	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		int n, j;
		printf("Case #%d:\n", it);
		cin >> n >> j;
		int cur =0;
		for (unsigned long long i = 0; i < (1 << (n-2)); i++) {
			ull tmp = (1<<(n-1)) | (i<<1) | 1;
			ull factors[11];
			int nfactors = 0;
			// check if tmp is jamcoin; it should be non-prime in all bases from 2-10
			for (int k = 2; k <= 10; k++) {
				ull basek = getbasek(tmp, k);






				// if base is nonprime save a facotr, increase factors
				for (ull ff = 2; ff *ff <= basek; ff++) {
					if (basek%ff == 0) {
						factors[k] = ff;
						nfactors++;
						break;
					}
				}
			}




				if (nfactors == 9) {
					print_binary(tmp);
					for (int k = 2; k <= 10; k++) {
						cout << " " << factors[k];
					}
					puts("");
					cur++;
				}
				if (cur==j)
					break;
		}



	}

	return 0;

}
