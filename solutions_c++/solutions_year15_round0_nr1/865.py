#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
char str[1100];
int s[1100];
int n;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    int ans,cas;
    scanf("%d",&T);
    cas=0;
    while(T--)
    {
        scanf("%d%s",&n,str);
        ans=0;
        for(int i=0;i<=n;i++)
        {
            s[i]=str[i]-'0';
        }
        for(int i=1;i<=n;i++)
        {
          //  printf("%d ",s[i]);
            if(s[i]) ans=max(ans,i-s[i-1]);
            s[i]+=s[i-1];

        }
        //cout << endl;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
