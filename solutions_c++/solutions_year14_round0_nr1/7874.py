#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int mat1[5][5],mat2[5][5];
    scanf("%d",&t);
    for(int cc=0;cc<t;cc++)
    {
        int r1;
        scanf("%d",&r1);
        r1--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat1[i][j]);
        int r2;
        scanf("%d",&r2);
        r2--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat2[i][j]);
        int f[20]={0};
        for(int i=0;i<4;i++)
            f[mat1[r1][i]]=1;
        int cnt=0,ans=-1;
        for(int i=0;i<4;i++)
            if(f[mat2[r2][i]]==1)
            {
                //printf("%d\n",ans);
                ans=mat2[r2][i];
                cnt++;
            }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",cc+1);
        if(cnt==1)
            printf("Case #%d: %d\n",cc+1,ans);
        if(cnt>1)
            printf("Case #%d: Bad magician!\n",cc+1);
    }
    return 0;
}
