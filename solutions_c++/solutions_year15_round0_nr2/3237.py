#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
using namespace std;
const int maxn = 1e3 + 5;
int p[maxn],D;
bool ok(int q,int mc)
{
    if(mc>=q)return false;
    int End = q - mc; 
    int lft = mc;
    for(int i = D-1; i >= 0; i--) {
        if(p[i]<End)return true;
        lft -= (p[i]-1)/End;
        if(lft<0)return false;
    }
    return true;
}
bool check(int q)
{
    for(int i = q-1;i>=0;i--)if(ok(q,i))
        return true;
    return false;
}
int solve()
{
    int L = 1,R = 1000+5;
    while(L < R) {
        int mid = (L+R)>>1;
        if(check(mid))R = mid;
        else L = mid + 1;
    }
    return L;
}
int main(int argc, char const *argv[])
{
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; ++cas) {
        scanf("%d",&D);
        for(int i = 0; i < D; ++i)
            scanf("%d", p+i);
        sort(p,p+D);
        printf("Case #%d: %d\n",cas,solve());
    }
    return 0;
}