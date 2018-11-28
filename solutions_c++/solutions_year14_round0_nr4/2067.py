#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<cstdlib>
using namespace std;

const int MAXN = 1100;

void solve()
{
    double naomi[MAXN],ken[MAXN];
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%lf",naomi+i);
    for(int i=0;i<n;i++)scanf("%lf",ken+i);
    int ans_deceive =0,ans_war =0;
    sort(naomi,naomi+n);
    sort(ken,ken+n);

    bool used[MAXN];
    bool ken_win_flag;
    memset(used,0,sizeof(used));
    for(int i=0;i<n;i++)
    {
        ken_win_flag = false;
        for(int j=0;j<n;j++)
        {
            if(used[j]==false && naomi[j]>ken[i])
            {
                ken_win_flag=true;
                used[j]=1;
                break;
            }
        }
        if(ken_win_flag==true)
        {
            ans_deceive ++;
        }
    }



    memset(used,0,sizeof(used));
    for(int i=0;i<n;i++)
    {
        ken_win_flag = false;
        for(int j=0;j<n;j++)
        {
            if(used[j]==false && ken[j]>naomi[i])
            {
                ken_win_flag = true;
                used[j]=1;
                break;
            }
        }
        if(ken_win_flag==false)
        {
            ans_war++;
        }
    }
    printf("%d %d\n",ans_deceive,ans_war);

}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
