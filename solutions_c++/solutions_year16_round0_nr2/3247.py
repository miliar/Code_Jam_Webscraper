#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;


int main()
{
  //  freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);
    int t,n,ans;
    char a[1001];
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        ans=0;
        scanf(" %s",a);
        n=strlen(a);
        for(int i=1;i<n;++i)
            if(a[i]!=a[i-1])
                ++ans;
        if(a[n-1]=='-')
            ++ans;
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
