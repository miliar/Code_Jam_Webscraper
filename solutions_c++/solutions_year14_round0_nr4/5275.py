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

int day[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int sum[13];
int n,m;

int main() {
    for (int i=1; i<=12; i++) sum[i]=sum[i-1]+day[i];
    while (cin >> n >> m) {
        if (m<1 || m>12 || n<1 || n>day[m]) puts("Impossible");
        else {
            int ans=(sum[m-1]+n)%7;
            if (ans==0) ans=7;
            cout << ans << endl;
        }
    }
    return 0;
}

