#include<cstdio>
using namespace std;

int main()
{
//    freopen("input.txt","r",stdin);
    int i,j,k,t,A,B,K,ans;

    scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        scanf("%d%d%d",&A,&B,&K);
        ans = 0;
        for(j=0;j<A;j++)
        {
            for(k=0;k<B;k++)
            {
                if((j&k) < K)
                {
//                    printf("<%d,%d>\n",j,k);
                    ans++;
                }
            }
//            printf("\n");
        }
        printf("Case #%d: %d\n", i+1, ans);
    }
    return(0);
}
