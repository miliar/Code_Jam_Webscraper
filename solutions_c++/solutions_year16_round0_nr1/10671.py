#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <iomanip>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>
#include <functional>

#define pb push_back
#define mk make_pair
#define sqr(N) ((N)*(N))
#define F first
#define S second
#define maxn 200010

using namespace std;

typedef long long ll;


int T;

long long n;
bool met[10];

void add(long long val) {
    while (val > 0) {
        met[val % 10] = 1;
        val /= 10;
    }
}

bool check() {
    int cnt = 0;
    for (int i = 0; i <= 9; ++i)
        cnt += met[i];
    return cnt == 10;
}

long long solve() {
    
    cin >> n;
    memset(met, 0, sizeof(met));
    if (n == 0) return -1;
    add(n);
    if (check()) {
        return n;
    }
    long long oldN = n;
    for (int i = 1; ;++i) {
        add(n+oldN);
        if (check()) {
            return n+oldN;
        }
        n = n + oldN;
    }
    return 0;
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int it = 1; it <= T; ++it) {
        
        
        long long ans = solve();
        if (ans == -1)
            cout << "Case #" << it << ": " << "INSOMNIA" << endl;
        else cout << "Case #" << it << ": " << ans << endl;
    }
    
    
    return 0;
}