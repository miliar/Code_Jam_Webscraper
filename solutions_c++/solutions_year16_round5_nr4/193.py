#include <bits/stdc++.h>

using namespace std;

int N, L;
char S[10001];

void _main(int TEST)
{
    scanf("%d%d", &N, &L);
    bool impossible=false;
    for(int i=0; i<N; i++)
    {
        scanf("%s", S);
        bool all=true;
        for(int j=0; j<L; j++)
            all&=S[j]=='1';
        if(all)
            impossible=true;
    }
    scanf("%s", S);
    if(impossible)
        printf("IMPOSSIBLE\n");
    else
    {
        printf("0");
        for(int i=0; i<L-1; i++)
            printf("?");
        printf(" ");
        for(int i=0; i<L-1; i++)
            printf("10");
        printf("?");
        for(int i=0; i<L-1; i++)
            printf("1");
        printf("\n");
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("D-small-attempt2.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
