#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define LL long long
#define N 10007
using namespace std;
int a[N];
int main()
{
    freopen("AA-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    int run,n,x,ans;
    scanf("%d",&run);
    for (int cas=1;cas<=run;cas++)
    {
        scanf("%d%d",&n,&x);
        for (int i=0;i<n;i++)
            scanf("%d",a+i);
        sort(a,a+n);
        ans=n;
        for (int i=0,j=n-1;i<j;j--)
            if (a[i]+a[j]<=x)
                i++,ans--;
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}

