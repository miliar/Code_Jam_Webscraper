#include<cstdio>

int a[10][10],b[10][10];
int main()
{
//    freopen("in.in","r",stdin);
//    freopen("ans.in","w",stdout);
    int T,Case=1;
    scanf("%d",&T);
    while(T--)
    {
        int ans1,ans2;
        scanf("%d",&ans1);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&ans2);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        int ans=-1,id;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a[ans1][i]==b[ans2][j])
                {
                    ans++;
                    id=i;
                }
            }
        }
        printf("Case #%d: ",Case++);
        if(ans==-1)
        {
            puts("Volunteer cheated!");
        }
        if(ans==0)
        {
            printf("%d\n",a[ans1][id]);
        }
        if(ans>0)
        {
            puts("Bad magician!");
        }
    }
    return 0;
}
