#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,f[5][5],s[5][5],cf,cs,cc,id;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        cc=0;
        id=0;
        scanf("%d",&cf);
        cf--;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%d",&f[j][k]);
            }
        }
        scanf("%d",&cs);
        cs--;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%d",&s[j][k]);
            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(f[cf][j]==s[cs][k])
                {
                    cc++;
                    id=f[cf][j];
                }
            }
        }
        if(cc==1)
        {
            printf("Case #%d: %d\n",i+1,id);
        }
        else if(cc==0)
        {
            printf("Case #%d: Volunteer cheated!\n",i+1);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",i+1);
        }
    }
    return 0;
}
