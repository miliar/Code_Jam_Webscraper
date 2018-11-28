#include <cstdio>
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int a[10][10],b[10][10];
    int T,n,m;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int c[10],d[10];
        scanf("%d",&n);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
            if(i==n-1)
            {
                for(int j=0;j<4;j++)
                    c[j]=a[i][j];
            }
        }
        int ans=0,tmp=0;
        scanf("%d",&m);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
            }
            if(m==i+1)
            {
                for(int j=0;j<4;j++)
                {
                    d[j]=b[i][j];
                }
            }
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(c[i]==d[j]){
                    ans++;
                    tmp=c[i];
                }
            }
        }
        if(ans==1)
            printf("Case #%d: %d\n",cas,tmp);
        else if(ans>1)
            printf("Case #%d: Bad magician!\n",cas);
        else if(ans==0)
            printf("Case #%d: Volunteer cheated!\n",cas);

    }
}
