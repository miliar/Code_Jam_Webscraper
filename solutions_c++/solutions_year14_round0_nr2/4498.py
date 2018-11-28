#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <climits>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i ++)
#define mem(s, v) memset(s, v, sizeof(s))
#define sz(v) (int)v.size()
#define pb push_back
#define mp make_pair

int main() {
    freopen("/Users/youhangtian/Downloads/B-large.in", "r", stdin);
    freopen("/Users/youhangtian/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int ca = 1; ca <= T; ca ++) {
        double c, f, x;
        cin >> c >> f >> x;
        
        double n = (f * x / c - f - 2) / f;
        int nn = (int)n;
        if (nn < n) nn ++;
        
        double res = 0;
        double rate = 2.0;
        for (int i = 1; i <= nn; i ++) {
            res += c / rate;
            rate += f;
        }
        res += x / rate;
        
        printf("Case #%d: %.7f\n", ca, res);
    }
    
    return 0;
}