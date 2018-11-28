#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int n, a[100100];

void solve(int num) {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) scanf("%d", a + i);
    int mx = *max_element(a, a + n);
    int ans = mx;
    for(int i = mx; i >= 1; i--) {
        int cur = 0;
        for(int j = 0; j < n; j++) {
            if(a[j] <= i) continue;
            if(a[j] % i == 0) cur += a[j] / i - 1;
            else cur += a[j] / i;
        }
        ans = min(ans, i + cur);
    }
    printf("Case #%d: %d\n", num, ans);
}

int main(){
    
    int t;
    
    scanf("%d", &t);
    
    for(int i = 1; i <= t; i++) {
        solve(i);
    }
        
    return 0;
}
