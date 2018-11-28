#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define eps 1e-8

int t, n;
LL p;

LL work(int n, LL p) {
    if (p == (1LL << n)) return (1LL << n) - 1;
    if (p >= (1LL << (n - 1))) return (1LL << n) - 2;
    return work(n - 1, p) * 2;
}

LL work1(int n, LL p) {
    if (p == (1LL << n)) return (1LL << n) - 1;
    if (p <= (1LL << (n - 1))) return 0;
    return work1(n - 1, p - (1LL << (n - 1))) * 2 + 1;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        cin>>n>>p;
        LL ans = work1(n, p);
        if (ans != 0 && ans != (1LL << n) - 1) ans *= 2;
        cout<<"Case #"<<ca<<": "<<ans<<" "<<work(n, p)<<endl;
    }
    return 0;
}
