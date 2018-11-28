#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>

using namespace std;

int a[5][5],b[5][5];

int main()
{
#ifdef PKWV
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // PKWV
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
        int a1;
        scanf("%d",&a1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        int b1;
        scanf("%d",&b1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        int l=0;
        int ans[20];
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a[a1][i]==b[b1][j])
                {
                    ans[l++]=a[a1][i];
                }
            }
        }
        printf("Case #%d: ",cas++);
        if(l==1)
        {
            printf("%d\n",ans[0]);
        }else if(l==0)
        {
            printf("Volunteer cheated!\n");
        }else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
