#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B_output_large.txt","w",stdout);
    int T;
    char s[1000];
    int a[1000];
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        scanf("%s",s);
        int N=strlen(s);
        int ans=0;
        for (int i=0;i<N;i++)
        {
            if (s[i]=='-') a[i]=0;
            else a[i]=1;
            if (i>0 && s[i]!=s[i-1]) ans++;
        }
        if ((a[0]+ans)%2==0) ans++;
        printf("Case #%d: %d\n",index,ans);
    }
    return 0;
}
