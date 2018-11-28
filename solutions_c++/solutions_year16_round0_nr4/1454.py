#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const int N = 1 << 24;

int t,k,c,s;

void init()
{
    scanf("%d %d %d",&k,&c,&s);
}

void work()
{
    for(int i = 1;i <= s;i++) printf(" %d",i);
    printf("\n");
}

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);

    int T;
    cin>>T;

    for(int i = 1;i <= T;i++)
    {
        init();
        printf("Case #%d:",i);
        work();
    }
    return 0;
}
