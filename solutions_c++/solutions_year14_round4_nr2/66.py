#include <cstdio>
#include <algorithm>
using namespace std;

int n;
int a[1005], b[1005];

void read() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
}

void solve() {
    int ans = 0;
    
    for (int i = 0; i < n; i++) {
        int left = 0, right = 0;
        
        for (int j = 0; j < i; j++) {
            if (a[j] > a[i]) ++ left;
        }
        for (int j = i + 1; j < n; j++) {
            if (a[j] > a[i]) ++ right;
        }
        
        ans += min(left, right);
    }
    
    printf ("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
