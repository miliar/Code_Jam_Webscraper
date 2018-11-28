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

string s;
int main() {
    int i, n, t;
    cin >> t;
    int cs = 1;
    while (t--) {
        cin >> n >> s;
        int ccnt = 0;
        int ans = 0;
        for (i = 0; i <= n; i++) {
            ans += max(0, i - ccnt - ans);
            ccnt += (s[i] - '0');
        }
        printf("Case #%d: %d\n", cs++, ans);
    }

    return 0;
}

