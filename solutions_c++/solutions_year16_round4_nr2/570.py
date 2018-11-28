#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <stack>
#include <map>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <unordered_map>
#include <cstring>
#include <ctime>
#include <bitset>
#include <cassert>
using namespace std;

#include "Infint.h"
//#include "euler.h"

long double mem[205][500];
vector<long double> v; // REMEMBER TO CLEAR / INITIALIZE!

long double dp(int pos, int n) { // n = number of points, +1 if vote for, 0 otherwise
    if (pos == -1) {
        if (n == 0) return 1;
        else return 0;
    }
    if (mem[pos][n+250] != -1) return mem[pos][n+250];
    mem[pos][n+250] = dp(pos-1, n-1) * v[pos] + dp(pos-1, n) * (1.0-v[pos]);
//    printf("dp(%d, %d) = %Lf\n", pos, n, mem[pos][n]);
    return mem[pos][n+250];
}

long double prob() { // compute probability of draw given probabilities given
    memset(mem, -1, sizeof mem);
    return dp(v.size()-1, v.size()/2);
}

vector<long double> a;
long double ans;

int main() {
    freopen("/Users/tianyi/Desktop/input.txt", "r", stdin);
//    freopen("/Users/tianyi/Desktop/output.txt", "w", stdout);
    
    int tc; scanf("%d", &tc);
    for (int tcn = 1; tcn <= tc; tcn++) {
        printf("Case #%d: ", tcn);
        int n, k;
        scanf("%d%d", &n, &k);
        a.clear();
        for (int i = 0; i < n; i++) {
            long double tmp; scanf("%Lf", &tmp);
            a.push_back(tmp);
        }
        
        ans = 0;
        
        // Sort and only add first i and last k-i
        sort(a.begin(), a.end());
        for (int i = 0; i <= k; i++) {
            v.clear();
            for (int j = 0; j < i; j++) v.push_back(a[j]);
            for (int j = n-k+i; j < n; j++) {
                v.push_back(a[j]);
            }
            
            ans = max(ans, prob());
        }
        
        printf("%Lf\n", ans);
    }
    return 0;
}