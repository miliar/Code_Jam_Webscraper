#include <bits/stdc++.h>
using namespace std;

bool solve(char *s,int num)
{
    int sum = num;
    for(int i = 0; s[i]; i ++) {
        int x = s[i] - '0';
        if(sum >= i) sum += x;
        else if(x) return false;
    }
    return true;
}
        
int solve()
{
    char s[1010];
    scanf("%*d%s",s);
    for(int i = 0; i < 10; i ++) {
        if(solve(s,i)) return i;
    }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        int ans = solve();
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
