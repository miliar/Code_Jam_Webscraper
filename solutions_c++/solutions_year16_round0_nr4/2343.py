#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <math.h>
using namespace std;

int main() {
	FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("D-small.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ":";
		int k, c, s;
		cin >> k;
        cin >> c;
        cin >> s;
        if (c==1) {
            if (s < k) {
                cout << " IMPOSSIBLE" << endl;
            }
            else {
                for (int i = 1; i <= k; i++) {
                    cout << " " << i;
                }
                cout << endl;
            }
        }
        else {
            int half = ceil(k/2.0);
            int diff = k-1;
            if (s < half) {
                cout << " IMPOSSIBLE" << endl;
            }
            else {
                for (int i = 0; i < half; i++) {
                    cout << " " << k;
                    k += diff;
                }
                cout << endl;
            }
        }
	}
	exit(0);
}