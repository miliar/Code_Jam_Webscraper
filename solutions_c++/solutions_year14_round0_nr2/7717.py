#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define sz(v) ((int)(v).size())
#define pb push_back
#define clr(x,a) memset(x,a,sizeof(x))
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int casenum;
    cin >> casenum;
    for(int ca = 1; ca <= casenum; ca++)
    {
        double C, F, X;
        cin >> C >> F >> X;
        double cur = 2.0;
        double ans = 1e18;
        double t = 0;
        for(int i = 0; i <= 100000; i++)
        {
            ans = min(ans, t + X/cur);
            t += C/cur;
            cur += F;
        }
        printf("Case #%d: %.7f\n", ca, ans);
    }
    return 0;
}

