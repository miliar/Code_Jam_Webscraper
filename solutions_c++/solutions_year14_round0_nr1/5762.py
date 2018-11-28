#include <iostream>
#include <cstdio>
using namespace std;
int a[5][5];
int b[5][5];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("test.out","w",stdout);
    int t;
    int m;
    int n;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d",&m);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        int ans=0;
        int cnt=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a[m][i]==b[n][j])
                {
                    //cout<<a[m][i]<<endl;
                    ans=a[m][i];
                    cnt++;
                }
            }
        }
        if(cnt==1)
        {
            printf("Case #%d: %d\n",cas++,ans);
        }
        else if(cnt>=2)
        {
            printf("Case #%d: Bad magician!\n",cas++);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n",cas++);
        }
    }
    return 0;
}
