#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long ll;
const int maxn=5;
int a[maxn][maxn];
int b[maxn][maxn];
int n,m;
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("out.txt","w",stdout);
    int tt;
    int cnt=0;
    scanf("%d",&tt);
    while(tt--)
    {
        cnt++;
        printf("Case #%d: ",cnt);
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            scanf("%d",&b[i][j]);
        }
        int tmp=0;
        int ans=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(a[n][i]==b[m][j])
                {
                    tmp++;
                    ans=a[n][i];
                }
            }
        }
        if(tmp==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(tmp==1)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("Bad magician!\n");
        }

    }
    return 0;
}
