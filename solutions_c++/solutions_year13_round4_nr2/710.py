#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

typedef long long LL;
#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

LL WW(LL n, LL p, int r) {
    if (p == 1) return 0;
    if (p == n) return n-1;
    LL ret = 0, k = 2, kk = 4, ran = n/2;
    //cout<<p<<" .. "<<n<<"\n";
    while (1) {
        if (p <= ran) return ret;
        //cout<<p<<" "<<ran<<"\n";
        ret += k;
        ran = ran + n/kk;
        k = k * 2;
        kk = kk * 2;
    }
}

LL CW(LL n, LL p, int r) {
    if (p == 1) return 0;
    if (p == n) return n-1;
    LL ret = n-2;
    LL k = 2;
    while (1) {
        if (p >= n/2 && p <= n-1) return ret;
        n /= 2;
        ret -= k;
        k = k * 2;
    }
    return 0;
}

int main() {
    int noOfTestCases;
    scanf("%d", &noOfTestCases);
    for (int testCase = 1; testCase <= noOfTestCases; testCase++) {
        printf("Case #%d: ",testCase);
        LL n, p;
        cin>>n>>p;
        //n = 5; p = testCase;
        LL team = (1LL<<n);
        LL couldWin = CW(team, p, n);
        LL willWin = WW(team, p, n);
        cout<<willWin<<" "<<couldWin<<"\n";
    }
	return 0;
}
