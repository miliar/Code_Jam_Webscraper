#include <iostream>
#include <string>

#define INF 1000000000.0
#define MAX_N 100
#define PA pair<long double, long double>

using namespace std;

int tests, n, m, answer;
long double inff;
long double v, x, l, r, mi, tmp1, tmp2;
long double xx, vv;
PA a[MAX_N];

int main() {
    inff = INF;
    inff *= inff;
    cin >> tests;
    for (int test = 0 ; test < tests ; test ++) {
        cin >> n >> v >> x;
	for (int i = 0 ; i < n ; i ++) {
	    cin >> tmp1 >> tmp2;
	    a[i] = PA(tmp2, tmp1);
	}
	sort(a, a + n);
	/*for (int i = 0 ; i < n ; i ++) {
	    cout << "A[" << i << "]: " << a[i].first << "XXX" <<a[i].second;
	    }*/
	l = 0.0;
	r = inff;
	while (r - l > 1e-9) {
	    mi = (l + r) / 2.0;
	    xx = 0;
	    vv = 0;
	    for (int i = 0 ; i < n ; i ++) {
		if (v > vv + a[i].second * mi) {
		    xx += a[i].first * a[i].second * mi;
		    vv += a[i].second * mi;
		} else {
		    xx += a[i].first * (v - vv);
		    vv = v;
		}
	    }
	    //   cout << "XXXXX" << mi << " -- " << xx/vv << "----" << v << endl;
	    //cout << (xx/vv <= x) << (vv == v) << endl;
	    if ((vv >= v - 1e-15) and (xx/vv <= x + 1e-15)) {
		xx = 0;
		vv = 0;
		for (int i = n - 1 ; i >= 0 ; i --) {
		    if (v > vv + a[i].second * mi) {
			xx += a[i].first * a[i].second * mi;
			vv += a[i].second * mi;
		    } else {
			xx += a[i].first * (v - vv);
			vv = v;
		    }
		}
		//	cout << "YYYYY" << mi << " -- " << xx/vv << endl;
		//cout << (xx/vv >= x) << endl;
		if ((xx/vv + 1e-15 >= x)) {
		    r = mi;
		} else {
		    l = mi;
		}
	    } else {
		l = mi;
	    }
	}
        cout << "Case #" << test + 1 << ": ";
	if (r == inff) {
	    cout << "IMPOSSIBLE" << endl;
	} else {
	    //   cout << r << endl;
	    printf("%.8Lf\n", r);
	}
    }
    return 0;
}
