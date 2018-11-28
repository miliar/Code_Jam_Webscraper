#include <cstdio>
using namespace std;

#define FOR(i, n) for(int i=0;i<n;i++)
#define FORR(i, n) for(int i=n;i>=0;i--)
#define FOR1(i, n) for(int i=1;i<=n;i++) 
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define ll long long

bool digits[10];

int extract (long long a) {
    int ans = 0;
    while(a > 0) {
        int digit = a % 10LL;
        if(!digits[digit]) ans++;
        digits[digit] = true;
        a /= 10LL;
    }
    return ans;
}

int main () {
    int t;
    scanf("%d", &t);
    FOR1(c, t) {
        int n, cnt = 0;
        scanf("%d", &n);
        printf("Case #%d: ", c);
        if(!n) {
            printf("INSOMNIA\n");
            continue;
        }
        long long a = 1LL * n;
        while(true) {
            cnt += extract(a);
            if(cnt == 10) break;
            a += 1LL * n;
        }
        printf("%lld\n", a);
        FOR(i, 10) digits[i] = false;
    }
}