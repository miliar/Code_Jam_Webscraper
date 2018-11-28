#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;


void solve()
{
    int n;
    scanf("%d ",&n);
    char ch;
    int ans = 0;
    scanf("%c",&ch);
    int k = atoi(&ch);
    for (int i = 1; i <= n; i++){
        int r;
        scanf("%c",&ch);
        r = atoi(&ch);
        if ( k < i) ans = max(i-k,ans);
        k += r;
    }
    printf("%d\n",ans);
}

int main()
{
    cout.sync_with_stdio(false);
    int cases;
    scanf("%d",&cases);
    for (int i = 1; i <= cases; i++)
    {
        printf("Case #%d: ",i); 
        solve();
    }
    return 0;
}
