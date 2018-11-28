#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
		int foo[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		int track = 0;
		int n;
		cin >> n;
		int num = 0;
		int i = 1;
		if (n != 0) {
			while (track < 10) {
			num = i*n;
			while (num > 0) {
				int index = num%10;
				if (index == foo[index]) {
					track += 1;
					foo[index] = -1;
				}
				num = num/10;
			}
			i++;
			}
			cout << "Case #" << t << ": ";
			cout << (i-1)*n << endl;
		} else {
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}

	}
	exit(0);
}
