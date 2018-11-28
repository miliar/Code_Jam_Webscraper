#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int w[105][105],ans[105][105];
int n,m;

void change()
{
    int i,j,ma;
    for(i=0;i<n;i++)
    {
        ma = 0;
        for(j=0;j<m;j++)
        ma = max(ans[i][j],ma);
        for(j=0;j<m;j++)
        w[i][j] = ma;
    }
    for(j=0;j<m;j++)
    {
        ma = 0;
        for(i=0;i<n;i++)
        ma = max(ans[i][j],ma);
        for(i=0;i<n;i++)
        w[i][j] = ma > w[i][j]? w[i][j] : ma;
    }
}

bool judge()
{
    int i,j;
    for(i=0;i<n;i++)
    for(j=0;j<m;j++)
    if(ans[i][j]!=w[i][j])
    return false;
    return true;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,cas = 1;
    cin >> t;
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        scanf("%d",&ans[i][j]);
        change();
        printf("Case #%d: ",cas++);
        if(judge())
        cout << "YES" << endl;
        else
        cout << "NO" << endl;
    }
    return 0;
}
