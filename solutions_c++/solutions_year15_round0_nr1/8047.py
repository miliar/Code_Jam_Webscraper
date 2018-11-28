#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;


int T, n;
int a[100000];
char s[100000];
int main() {
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
//    freopen("/home/zyc/Documents/Code/cpp/in","r",stdin);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d", &n);
        scanf("%s", s);
        int now = s[0] - '0', ans = 0;
        for(int i = 1; i <= n; i++)
        {
            if(i > now)
            {
                ans += i - now;
                now = i;
            }
            now += s[i] - '0';
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
