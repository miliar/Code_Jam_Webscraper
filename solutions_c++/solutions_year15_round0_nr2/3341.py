#include <stdio.h>
#include <queue>
using namespace std;

int a[100000];
int dp[2000][2000];

void solve()
{
    
    int n;
    scanf("%d",&n);
    for (int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    int ans = (1<<28);
    for (int d=1;d<=1000;d++)
    {   
        int tmp = d;
        for (int i=0;i<n;i++) tmp += dp[a[i]][d];
        ans = min(ans,tmp);
    }

    printf("%d\n",ans);
}

void prepare()
{

    for (int d=1;d<=1000;d++)
        for (int i=1;i<=1000;i++)
    {
            dp[i][d] = i-d;
            if ( i < d ) dp[i][d] = 0;
            for (int j=i-1;j>=1;j--)
            {
                dp[i][d] = min(1 + dp[j][d] + dp[i-j][d], dp[i][d]);
            }
    }


}


int main()
{

    prepare();
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {

        printf("Case #%d: ",i);
        solve();
    }
    return 0;

}
