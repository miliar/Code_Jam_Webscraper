#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("A-Large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("outputLarge.txt", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		int n;
		cin >> n;
		int m[n];
		for (int i=0;i<n;i++) cin >> m[i];

		int y=0;
		int maxGap=0;
		for (int i=0;i<n-1;i++) {
            if (m[i+1]<m[i]) {
                    int gap = m[i]-m[i+1];
                    y+= gap;
                    if (gap>maxGap) {
                            maxGap = gap;
                    }
            }
		}

		int z = 0;
		for (int i=0; i<n-1 ;i++) {
            if (m[i]-maxGap<0) {
                z+=m[i];
            }
        else  {
            z+=maxGap;
        }
		}

		cout << y << " " << z << "\n";

	}
	exit(0);
}
