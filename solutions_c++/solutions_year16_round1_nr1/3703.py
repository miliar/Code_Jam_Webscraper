#include <bits/stdc++.h>
#define LL long long
using namespace std;

const int maxn = 1000 + 10;
char s[maxn],ans[maxn],tmp[maxn],tp[maxn];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas = 0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s",s);
        int n = strlen(s);
        ans[1]=s[0];
        tmp[0]=s[0];
        for (int i=1;i<n;i++)
        {
            ans[0] = s[i];
            tmp[i] = s[i];
            ans[i+1] = NULL;
            tmp[i+1] = NULL;
            if (strncmp(ans,tmp,i+1) < 0)
            {
                strcpy(ans,tmp);
                for (int j=i+1;j>0;j--) ans[j] = ans[j-1];
            }
            else
            {
                strcpy(tmp,ans);
                for (int j=i+1;j>0;j--) ans[j] = ans[j-1];
            }
        }
        ans[n+1] = NULL;
        printf("Case #%d: %s\n",++cas,ans+1);
    }

    return 0;
}
