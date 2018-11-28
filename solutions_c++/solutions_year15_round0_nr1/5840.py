#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAX_N 1000

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    
    char S[MAX_N + 1];
    int n, i, p, ans;
    int test = 0;
    
    while (t--) {
        scanf("%d %s", &n, S);

        p = 0, ans = 0;
        for (i = 0; i <= n; i++) {
            if (S[i] > '0' && p < i) {
                ans += (i - p);
                p += (i - p);
                //cout << i << " " << p << endl;
            }
            p += (S[i] - '0');
        }
        
        test++;
        printf("Case #%d: %d\n", test, ans);
    }
    
    return 0;
}


