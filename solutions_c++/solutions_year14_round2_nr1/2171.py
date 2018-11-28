#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
char word[101];
struct myStruct
{
    char cha;
    int app;
}A[101][101];
int N,M,T,L,S,Q,R,P[101],t,i,j,k,ok;
int maximum(int,int);
int main()
{
    freopen("ProblemA.in","r",stdin);
    freopen("ProblemA.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        ok=1;
        scanf("%d",&N);
        for(i=1;i<=N;i++)
        {
            scanf("%s",&word);
            M=strlen(word);
            L=0;
            for(j=0;j<=M-1;j++)
            {
                L++;
                A[i][L].cha=word[j];
                A[i][L].app=1;
                while(word[j]==word[j+1] && j+2<=M)
                {
                    A[i][L].app++;
                    j++;
                }
            }
            P[i]=L;
        }
        L=P[1];
        for(i=2;i<=N && ok;i++)
        {
            if(P[i]!=L)
            ok=0;
        }
        if(ok)
        {
            for(i=2;i<=N && ok;i++)
            {
                for(j=1;j<=L && ok;j++)
                {
                    if(A[i][j].cha!=A[1][j].cha)
                    ok=0;
                }
            }
            if(ok)
            {
                Q=0;
                for(j=1;j<=L;j++)
                {
                    S=0;
                    for(i=1;i<=N;i++)
                    S+=A[i][j].app;
                    S/=N;
                    for(i=1;i<=N;i++)
                    {
                        R=S-A[i][j].app;
                        if(R>=0)
                        Q+=R;
                        else
                        Q-=R;
                    }
                }
                printf("Case #%d: %d\n",t,Q);
            }
            else
            printf("Case #%d: Fegla Won\n",t);
        }
        else
        printf("Case #%d: Fegla Won\n",t);
    }
    return 0;
}
int maximum(int x,int y)
{
    if(x>=y)
    return x;
    else
    return y;
}
