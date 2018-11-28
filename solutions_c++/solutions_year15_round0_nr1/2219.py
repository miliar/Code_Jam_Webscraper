#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int T,a[1005],n,ans,TT,i,j,now;
char s[1005];
int main()
{
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&n);
        scanf("%s",s);
        for (i=0; i<=n; i++) a[i]=s[i]-'0';
        TT++;
        printf("Case #%d: ",TT); now=0;
        for (i=0; i<=n; i++)
          for (j=1; j<=a[i]; j++)
          {
              if (i<=now) now++; else {ans+=i-now; now=i; now++;}
          }
        cout<<ans<<endl;
        ans=0;
    }
    return 0;
}
