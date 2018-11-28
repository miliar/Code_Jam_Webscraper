#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int t, T, n, j, d[33];

bool tst(int n) {
    int i=0, p=0;
    while(n) {
        i += n % 2; n /= 2;
        p += n % 2; n /= 2;
    }
    return i == p;
}

int main() {
    scanf("%d", &T);
    scanf("%d%d", &n, &j);

    printf("Case #1:\n");

    ll k = (1<<(n-1)) + 1;
    for(int i=0; i<j; ++i, k += 2) {
        while(!tst(k)) k += 2;
        for(int x=k; x; x/=2) printf("%d", x%2);
        for(int x=2; x<11; ++x) printf(" %d", x+1);
        printf("\n");
    }
    return 0;
}
