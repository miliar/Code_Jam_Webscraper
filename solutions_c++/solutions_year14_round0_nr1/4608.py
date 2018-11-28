#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#define N 20
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int T;
    int mta[N][N],mtb[N][N];
    int ansa,ansb;
    scanf("%d",&T);
    int cas=1;
    for(cas=1;cas<=T;cas++)
    {
        scanf("%d",&ansa);
        ansa--;
        int i,j;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&mta[i][j]);
        scanf("%d",&ansb);
        ansb--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&mtb[i][j]);
        printf("Case #%d: ",cas);
        int ans=0;
        int ansv;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(mta[ansa][i]==mtb[ansb][j])
                {
                    ans++;
                    ansv=i;
                }
            }
        if(ans==1)
            printf("%d\n",mta[ansa][ansv]);
        else if(ans>1)
            printf("Bad magician!\n");
        else 
            printf("Volunteer cheated!\n");

    }
}
