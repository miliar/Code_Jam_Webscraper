#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

void solve()
{
    set<int> sr,sc;
    int r,x;
    scanf("%d",&r);
    for(int i = 1; i <= 4; i ++) {
        for(int j = 1; j <= 4; j ++) {
            scanf("%d",&x);
            if(i == r) sr.insert(x);
        }
    }
    scanf("%d",&r);
    int tot = 0,y = 0;
    for(int i = 1; i <= 4; i ++)
        for(int j = 1; j <= 4; j ++) {
            scanf("%d",&x);
            if(i == r) {
                if(sr.count(x)) tot ++,y = x;
            }
        }
    if(tot == 0) puts("Volunteer cheated!");
    else if(tot == 1) printf("%d\n",y);
    else puts("Bad magician!");
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
