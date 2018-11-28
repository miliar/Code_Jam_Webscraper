#include<cstdio>
int n,x[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d",&n);
        for(int i=1,c=0;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&c);
                if(i==n)
                    x[c]=1;
            }
        int all=0,ans=0;
        scanf("%d",&n);
        for(int i=1,c=0;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&c);
                if(i==n)
                {
                    all+=x[c];
                    if(x[c]>0)
                        ans=c;
                }
            }
        if(all>1)
            printf("Case #%d: Bad magician!\n",I);
        else if(all<1)
            printf("Case #%d: Volunteer cheated!\n",I);
        else
            printf("Case #%d: %d\n",I,ans);
        for(int i=1;i<=16;i++)
            x[i]=0;
    }
}
