#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long

int main() {
    int n;
    while (cin >> n) {
        int cnt=0;
        for (int i=1; i<=n; i++) {
            if (__gcd(i,n)==1) cnt++;
        }
        cout << cnt << endl;
    }
    return 0;
}
