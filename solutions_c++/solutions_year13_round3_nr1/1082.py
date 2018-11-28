#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

char s[100010];

int getv(char c) {
    if(c == 'a' || c == 'i' || c == 'o' || c == 'u' || c == 'e') return 0;
    return 1;
}

int f[1000010];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        long long ans = 0;
        int n;
        scanf("%s%d", s, &n);
        int l = strlen(s);
        memset(f, 0, sizeof(f));
        f[0] = getv(s[0]);
        for(int i = 1; i < l; i++) {
            if(getv(s[i]) == 0) f[i] = 0;
            else f[i] = f[i - 1] + 1;
        }
        int now = 0;
        for(int i = 0; i < l; i++) {
            while( now < l && min(f[now], now - i + 1) < n ) now++;
            if( min(f[now], now - i + 1) < n ) break;
            ans += (l - now);
        }

        printf("Case #%d: %lld\n", cnt++, ans);
    }

    return 0;
}
