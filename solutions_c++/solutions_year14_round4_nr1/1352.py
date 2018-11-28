#include <bits/stdc++.h>

using namespace std;

int N, X;
int files[10005];

void solve()
{
    scanf("%d%d", &N, &X);
    for(int i=0; i<N; i++)
        scanf("%d", files+i);
    sort(files, files+N);
    int l=0, r=N-1;
    int ans=0;
    while(l<r)
    {
        if(files[l]+files[r]<=X)
            l++, r--;
        else
            r--;
        ans++;
    }
    if(l==r)
        ans++;
    printf("%d\n", ans);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
