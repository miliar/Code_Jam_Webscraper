#include <bits/stdc++.h>

#define debug(x) cout << "> " << #x << " = " << x << endl;
#define debugat(arr, at) cout << "> " << #arr << "[" << at << "] = " << arr[at] << endl;

using namespace std;

typedef long long ll;

bool vis[30];

void mark(ll n) {
    while(n) {
        ll next = n % 10;
        vis[next] = true;
        n /= 10;
    }
}

bool allMarked() {
    for(int i = 0; i <= 9; ++i)
        if(!vis[i])
            return false;
    return true;
}

int main() {
    int tests;
    scanf("%d", &tests);

    for(int t = 1; t <= tests; ++t) {
        memset(vis, 0, sizeof vis);
        ll i;
        scanf("%lld", &i);
        printf("Case #%d: ", t);
        if(i == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        ll j;
        for(j = i; ; j += i) {
            mark(j);
            if(allMarked())
                break;
        }
        printf("%lld\n", j);
    }
    return 0;
}
