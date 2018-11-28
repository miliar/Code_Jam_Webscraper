#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
int a[10010];

int main()
{
    int o,cas=0;
    scanf("%d",&o);
    while(o--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=1; i<=n; i++) scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        int l=1,r=n,ans=0;
        while (l<=r)
        {
            while (r>l && a[r]+a[l]>m) {ans++; r--;}
            if (r==l) {ans++; break;}
            ans++; l++; r--;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}
