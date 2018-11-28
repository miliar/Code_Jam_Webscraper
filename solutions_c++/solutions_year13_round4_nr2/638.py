#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "B"

const int64 ONE = 1ll;

inline int64 glog(int64 a) {
	int64 res = 0;

	if (a == 0) return 0;

	int64 t = 1ll;
	while (t < a) {
		t = t+t;
		res++;
	}
	if (a != t) res--;

	return res;
}

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);


    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        cerr << t << ": ";
        int64 n, p;
        cin >> n >> p;

        int64 last = (ONE << n) - ONE;
        cerr << last << endl;

        int64 k1 = 0;
        if (p == (ONE << n)) {
        	k1 = last;
        }
        else {
            while (true) {
            	int64 ck = k1 + ONE;
    			
    			int64 ckk = glog(ck + ONE);

            	int64 sum = (ONE << n) - (ONE << (n-ckk));
            	//cerr << sum << endl;

            	if (p > sum) k1 = ck;
            	else break;
            }
        }

        int64 k2 = 0;
        while (p < (ONE << (n - glog(k2 + ONE)))) k2++;

        cout << k1 << " " << last - k2;
        printf("\n");
    }

    return 0;
}
