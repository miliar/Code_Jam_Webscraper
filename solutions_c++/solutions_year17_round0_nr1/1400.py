#include <bits/stdc++.h>
using namespace std;
const int maxn=1e3+100;

int T,N,K;
int pancake[maxn];
char inp[maxn];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&T);
    for(int kase=1;kase<=T;++kase)
    {
        scanf("%s %d",inp,&K);
        int cnt=0;
        N=strlen(inp);
        for(int i=0;i<=N-K;++i)
        {
            if(inp[i]=='+') continue;
            for(int j=0;j<K;++j)
            {
                if(inp[i+j]=='+')
                    inp[i+j]='-';
                else
                    inp[i+j]='+';
            }
            ++cnt;
        }
        for(int i=N-K+1;i<N;++i)
            if(inp[i]=='-')
                cnt=-1;
        printf("Case #%d: ",kase);
        if(cnt==-1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",cnt);
    }
    return 0;
}
