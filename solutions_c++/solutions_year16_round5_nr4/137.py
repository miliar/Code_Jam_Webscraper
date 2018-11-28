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

const int N = 100 + 5;

int n, l;
string s[N], b;

void solve() {
    scanf("%d %d", &n, &l);
    for(int i = 1; i <= n; i++) {
        cin >> s[i];
    }
    cin >> b;
    for(int i = 1; i <= n; i++) {
        if(s[i] == b) {
            puts("IMPOSSIBLE");
            return;
        }
    }
    for(int i = 1; i <= l; i++)
        printf("0?");
    printf(" ");
    for(int i = 1; i < l; i++)
        printf("1");
    printf("0");
    puts("");
}

int main () {
    
    freopen("in.txt", "r", stdin);
    freopen("small.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int t = 1; t <= tt; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
    
}