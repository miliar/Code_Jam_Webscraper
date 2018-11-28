#include<stdio.h>

int inp[1001];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,n,i,j,m,cnt,ans;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%d",&n);
        m=0;
        for (i=0;i<n;++i)
        {
            scanf ("%d",&inp[i]);
            if (inp[i]>m)m = inp[i];
        }
        ans = m;
        for (j=1;j<=m;++j)
        {
            cnt = 0;
            for (i=0;i<n;++i)
            {
                if(inp[i]>j)
                {
                    cnt += inp[i]/j-1;
                    if (inp[i]%j)cnt++;
                }
            }
            if(cnt+j < ans)ans = cnt+j;
        }
        printf("Case #%d: %d\n",ti+1,ans);
    }
    return 0;
}
