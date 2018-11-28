#include <cstdio>
#include<cstring>

using namespace std;
int A[5][5],B[5][5],E[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);

    int T,row1,row2;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        memset(E,0,sizeof(E));
        scanf("%d",&row1);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&A[i][j]);

        scanf("%d",&row2);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&B[i][j]);
        int cnt=0,ans=-1;
        for(int i=1;i<=4;i++) E[A[row1][i]]=1;
        for(int i=1;i<=4;i++) if(E[B[row2][i]]) {cnt++;ans=B[row2][i];}
        if(cnt==1) printf("Case #%d: %d\n",kase,ans);
        else if(cnt==0) printf("Case #%d: Volunteer cheated!\n",kase);
        else if(cnt>1) printf("Case #%d: Bad magician!\n",kase);
    }
    return 0;
}
