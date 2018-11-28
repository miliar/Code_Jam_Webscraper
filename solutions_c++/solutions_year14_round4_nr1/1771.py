#include <cstdio>
#include <algorithm>
using namespace std;
int T,N,X,M,S[10001],C[10001],Max,Pos,t,i,j;
int main()
{
    freopen("ProblemA.in","r",stdin);
    freopen("ProblemA.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        M=0;
        scanf("%d %d",&N,&X);
        for(i=1;i<=N;i++)
        scanf("%d",&S[i]);
        sort(S+1,S+N+1);
        for(i=1;i<=N;i++)
        {
            if(S[i]!=X+1)
            {
                j=i+1;
                while(j<=N && S[i]+S[j]<=X)
                j++;
                j--;
                M++;
                S[j]=X+1;
            }
        }
        printf("Case #%d: %d\n",t,M);
    }
    return 0;
}
