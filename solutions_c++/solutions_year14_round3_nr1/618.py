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
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

LL GCD (LL a, LL b) { if (!a) return b; return GCD(b%a, a);}

LL LCM(LL a, LL b) {
    LL g = GCD(a, b);
    return ((a/g * b/g) * g);
}

int is2p(LL a) {
    REP(i, 0, 50) {
        if (a == (1LL<<i)) return i+1;
    }
    return 0;
}

LL cnt(LL a, LL b) {
    if (a * 2 >= b) return 1;
    else return 1 + cnt(a, b/2);
}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(true);

    int testCases; cin>>testCases;
    REP(tests, 1, testCases+1) {
        cout<<"Case #"<<tests<<": ";
        LL a, b;
        scanf("%lld/%lld",&a, &b);
        LL g = GCD(a, b);
        a /= g;
        b /= g;
        if (!is2p(b)) cout<<"impossible\n";
        else cout<<cnt(a, b)<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

