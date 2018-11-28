#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <stack>
#include <cctype>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;
const double pi = 4*atan(1);
int gcd(int a, int b)   {return b == 0? a:gcd(b,a%b);}
int lcm(int a, int b)   {return a/gcd(a,b)*b;}

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
        ll n;
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", cas); 
            continue;
        }
        bool vis[10];
        memset(vis, 0, sizeof(vis));
        int cnt = 10;
        char temp[20];
        ll t = 1;
        ll tn = n;
        while(cnt > 0) {
            tn = n * t;
            t++;
            sprintf(temp, "%lld", tn);
            int len = strlen(temp);
            for(int i = 0; i < len; ++i) {
                if (vis[temp[i]-'0']) 
                    continue;
                vis[temp[i]-'0'] = true;
                --cnt;
            }
        }
        printf("Case #%d: %lld\n", cas, tn);

    }
    return 0;
}
