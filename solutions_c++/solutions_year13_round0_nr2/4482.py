/* 	Language C++
	Copyright Liang Yongqing all
*/

#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>

using namespace std;
#define fi first
#define se second
#define ll long long
#define INF 2000000000
#define eps 1e-12
#define maxn 105

int row[maxn],col[maxn],a[maxn][maxn];

int main()
{
	freopen("temp.in","r",stdin);
	freopen("temp.out","w",stdout);

    int Test,test; test=0;
    int n,m,i,j;

    scanf("%d",&Test);
    while (Test--)
    {
        printf("Case #%d: ",++test);

        scanf("%d%d",&n,&m);

        for (i=1;i<=n;i++) row[i]=0;
        for (j=1;j<=m;j++) col[j]=0;
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                scanf("%d",&a[i][j]);
                row[i]=max(row[i],a[i][j]);
                col[j]=max(col[j],a[i][j]);
            }
        }

        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                if (a[i][j]>=row[i]) continue;
                if (a[i][j]>=col[j]) continue;
                break;
            }
            if (j<=m) break;
        }
        if (i<=n) printf("NO\n");
            else printf("YES\n");
    }

	return 0;
}
