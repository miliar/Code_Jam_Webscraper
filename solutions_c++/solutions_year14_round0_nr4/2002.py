#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
using namespace std;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        int n;
        double a[2000],b[2000];
        scanf("%d",&n);
        for (int i=1; i<=n; i++)
            scanf("%lf",&a[i]);
        for (int i=1; i<=n; i++)
            scanf("%lf",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int i,j;
        int ans1,ans2;
        ans1=ans2=0;
        for (i=1,j=1;i<=n&&j<=n;)
        {
            if (a[i]>b[j])
                i++,j++,ans1++;
            else
                i++;
        }
        for (i=1,j=1;i<=n&&j<=n;)
        {
            if (b[j]>a[i])
                i++,j++,ans2++;
            else
                j++;
        }
        printf("Case #%d: %d %d\n",++cas,ans1,n-ans2);
    }
    return 0;
}
