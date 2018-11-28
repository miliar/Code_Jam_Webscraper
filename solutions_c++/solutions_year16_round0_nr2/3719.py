#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
//freopen("D.in","r",stdin);
//freopen("D.out","w",stdout);
#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define dbg(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define maxn 10001
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
char a[110];
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int ans;
    int T,caseno=0;
    scanf("%d",&T);
    while(T--)
    {
        ans = 0;
        scanf("%s",a);
        int i;
        for (i=0;i<strlen(a)-1;i++)
        {
            if (a[i]!=a[i+1]) ans++;
        }
        if (a[strlen(a)-1]=='-') ans++;
        printf("Case #%d: %d\n",++caseno,ans);
    }
    return 0;
}
