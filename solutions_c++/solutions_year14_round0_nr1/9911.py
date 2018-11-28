#include<stdio.h>
int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
  //  freopen("A-small-attempt0.in","r",stdin);
  //  freopen("A-small-attempt0.out","w",stdout);
    int T,a1,a2,a[4][4], b[4][4];

    scanf("%d",&T);
    for(int i=1; i<=T; i++)
    {
        int index = 0, val=0;
        scanf("%d",&a1);
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                scanf("%d",&a[j][k]);
            }
        }
        scanf("%d",&a2);
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                scanf("%d",&b[j][k]);
            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++){
                    if(a[a1-1][j]==b[a2-1][k])
                    {
                        ++index;
                        val=b[a2-1][k];
                    }
            }

        }
        if(index==0)
        {
            printf("Case #%d: Volunteer cheated!\n",i);
        }
        else if(index==1)
        {
            printf("Case #%d: %d\n",i,val);
        }
        else if(index>1)
        {
            printf("Case #%d: Bad magician!\n",i);
        }
    }
    return 0;
}
