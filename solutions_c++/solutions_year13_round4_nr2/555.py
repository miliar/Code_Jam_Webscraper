#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
typedef long long LL;

LL n, p, m, ans;
int T;

bool ff(LL k, LL p) {
	LL t = k, token = m;
	while (t > 0) {
		token /=2;
		if (p <= token) return false;
		p -= token;
		t = (t - 1) /2;
	}
	return true;
}

bool ff1(LL k, LL p) {
	LL t = m - k - 1, token = m;
	while (t > 0) {
		token /= 2;
		t = (t - 1) /2;
	}
	return (p >= token);
}

void gg1(LL l, LL r) {
    for (LL mid = (l+r)/2; l<=r; mid = (l+r)/2) {
        if (ff1(mid, p)) {
            ans = mid;
            l = mid+1;
        } else r = mid-1;
    }
}

void gg(LL l, LL r) {
    for (LL mid = (l+r)/2; l<=r; mid = (l+r)/2) {
        if (ff(mid, p)) {
            ans = mid;
            l = mid+1;
        } else r = mid-1;
    }
}

void work() {
    scanf("%I64d%I64d", &n, &p);
    m = (1ll << n);
    ans = 0;
    gg(1, (1ll << n) -1);
    cout << ans << " ";
    ans = 0;
    gg1(1, (1ll << n) -1);
    cout << ans << endl;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for(int _ = 1; _ <= T; _++) {
        printf("Case #%d: ", _);
        work();
    }
    return 0;
}

