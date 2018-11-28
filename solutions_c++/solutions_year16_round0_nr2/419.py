#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

const int MAXN = 10000;

int T;
char s[1000];
int f[1000];

void solve(int x)
{
    if( s[0] == '+' ) f[0] = 0;
    else f[0] = 1;

    for(int i=1;i<strlen(s);i++)
    {
        if( s[i] == '-' && s[i-1] == '+' )
            f[i] = f[i-1] + 2;
        else
            f[i] = f[i-1];
    }
    printf("Case #%d: %d\n",x,f[strlen(s)-1]);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output-large.txt","w",stdout);

    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        memset(f, 0, sizeof(f));
        scanf("%s",&s);
        solve(i);
    }

    return 0;
}
