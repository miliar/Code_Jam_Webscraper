#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int N = 1010;

int n, a[N];

int solve(int p){
    int ret = p;
    for(int i = 0; i < n; ++i) ret += (a[i] - 1) / p;
    return ret; 
}   
int main() {
    int T, sl, ans, cnt; 
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        cin >> n;
        for(int i = 0; i < n; ++i) cin >> a[i];
        int ans = ~0U >> 1;
        for(int i = 1; i <= 1000; ++i) ans = min(ans, solve(i));
        printf("Case #%d: %d\n", _, ans);
    }
    return 0;
}
