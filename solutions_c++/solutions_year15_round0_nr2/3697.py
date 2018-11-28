#include<bits/stdc++.h>
using namespace std;

#define LET(x, a)  __typeof(a) x(a)
#define TR(v, it) for(LET(it, v.begin()); it != v.end(); it++)
#define si(x) scanf("%d",&x)
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define INF 1000000000
#define MOD 1000000007
#define SET(x,y) memset(x,y,sizeof(x));
#define LL long long int
#define ULL unsigned LL
#define PII pair<int, int>

int a[1003];
int main() {
    int i, n, t, j;
    int cs = 1;
    cin >> t;
    while (t--) {
        cin >> n;
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        int ans = INF;
        for (i = 1; i <= ans; i++) {
            int cans = 0;
            for (j = 0; j < n; j++) {
                cans += (a[j] - 1) / i;
            }
            ans = min(ans, cans + i);
        }
        printf("Case #%d: %d\n", cs++, ans);
    }
    return 0;
}

