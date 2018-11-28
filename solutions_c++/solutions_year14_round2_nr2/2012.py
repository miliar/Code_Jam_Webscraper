#include <cstdio>
using namespace std;
int A,B,K,T,Sol,Ss,i,j,k,t,num;
int M[1001][1001];
int maximum(int,int);
int main()
{
    freopen("ProblemB.in","r",stdin);
    freopen("ProblemB.out","w",stdout);
    for(i=0;i<=1000;i++)
    {
        for(j=0;j<=1000;j++)
        {
            if(j>=1)
            M[i][j]=maximum(M[i][j-1],i&j);
            else
            M[i][j]=i&j;
        }
    }
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        Ss=0;
        scanf("%d %d %d",&A,&B,&K);
        for(i=0;i<=A-1;i++)
        {
            if(M[i][B-1]<K)
            Ss+=B;
            else
            {
                for(j=0;j<=B-1;j++)
                {
                    if((i&j)<K)
                    Ss++;
                }
            }
        }
        printf("Case #%d: %d\n",t,Ss);
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
