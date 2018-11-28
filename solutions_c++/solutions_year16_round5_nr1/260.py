#include <bits/stdc++.h>

using namespace std;

int N;
char S[20001];
char T[20001];
int dp[51][51];

int rec(int l, int r)
{
    if(l+1==r)
        return S[l]==S[r];
    int& ret=dp[l][r];
    if(ret!=-1)
        return ret;
    ret=rec(l+1, r-1)+(S[l]==S[r]);
    for(int i=l+2; i<=r; i+=2)
        ret=max(ret, rec(l, i-1)+rec(i, r));
    return ret;
}

void _main(int TEST)
{
    scanf("%s", S);
    N=strlen(S);
    memset(dp, -1, sizeof dp);
    //int rans=rec(0, N-1);
    int base=N/2;
    int M;
    int ans=0;
    while(1)
    {
        M=0;
        for(int i=0; i<N; i++)
        {
            if(i+1<N && S[i]==S[i+1])
                ans++, i++;
            else
                T[M++]=S[i];
        }
        if(N==M)
            break;
        N=M;
        for(int i=0; i<N; i++)
            S[i]=T[i];
    }
    //assert(ans==rans);
    ans+=base;
    printf("%d\n", ans*5);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
