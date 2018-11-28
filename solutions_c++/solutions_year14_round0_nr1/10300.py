#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    int t,T;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        int f,s,fa[10][10],se[10][10],re[6];
        scanf("%d",&f);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&fa[i][j]);
        scanf("%d",&s);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&se[i][j]);
        int count = 0,x;
        for(int i=0;i<4;i++)
        {
            //x = 0;
            for(int j=0;j<4;j++)
            {
                if(fa[f-1][i]==se[s-1][j])
                {
                    x = fa[f-1][i];
                    count++;
                }
            }
            //re[i] = x;
        }
//        for(int i=0;i<4;i++)
//        {
//            if(re[i]!=0)
//            {
//                count++;
//                x = re[i];
//            }
//        }
        if(count==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else if(count==1)
            printf("Case #%d: %d\n",t,x);
        else
            printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
