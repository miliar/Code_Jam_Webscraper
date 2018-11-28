#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
using namespace std;
int I,n,k,a[100005],i,l,ans,T;
int cmp(int i,int j) {return i<j;}
int main()
{
    scanf("%d",&T);
    for (I=1; I<=T; I++)
    {
        scanf("%d%d",&n,&k);
        for (i=1; i<=n; i++) scanf("%d",&a[i]);
        sort(a+1,a+n+1,cmp); l=1;
        for (i=n; i>=1; i--)
        {
            if (i<l) break;
            if (a[i]+a[l]<=k) l++;
            ans++;
        }
        printf("Case #%d: %d\n",I,ans);
        ans=0;
    }
    return 0;
}
