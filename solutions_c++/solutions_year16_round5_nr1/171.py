#include "iostream"
#include "algorithm"
#include "vector"
#include "set"
#include "map"
#include "cstring"
#include "string"
#include "vector"
#include "cassert"
#include "queue"
#include "cstdio"
#include "cstdlib"
#include "ctime"
#include "cmath"
#include "bitset"

using namespace std;

typedef long long ll;
typedef pair < ll, ll > ii;

const int N = 20000 + 5;

int n;
char s[N];

int calc(int tme) {
    int ans = 0;
    vector < ii > v;
    for(int i = 1; i < tme; i++) {
        if(v.size() and s[i] == v.back().first) {
            ans += v.back().second;
            v.pop_back();
        }
        else {
            v.push_back({s[i], 10});
        }
    }
    for(int i = tme; i <= n; i++) {
        if(v.size() and s[i] == v.back().first) {
            ans += v.back().second;
            v.pop_back();
        }
        else if(v.size()) {
            ans += v.back().second - 5;
            v.pop_back();
        }
        else {
            v.push_back({s[i], 10});
        }
    }
    return ans;
}

void solve() {
    scanf("%s", s + 1);
    n = strlen(s + 1);
    int ans = 0;
    for(int i = 1; i <= n + 1; i++)
        ans = max(ans, calc(i));
    printf("%d\n", ans);
}

int main () {
    
    freopen("in.txt", "r", stdin);
    freopen("large.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int t = 1; t <= tt; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
    
}