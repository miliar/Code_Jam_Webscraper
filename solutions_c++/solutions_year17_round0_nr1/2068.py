#include <bits/stdc++.h>

using namespace std;

char s[1005];

int main()
{
    freopen("Al.out","w",stdout);
    int T,t,sz;
    int N,count;
    int i,j;
    bool found;
    scanf("%d",&T);
    for(t=1;t<=T;++t)
    {
        scanf("%s %d",s,&N);
        count = found = 0;
        sz = strlen(s);
        printf("Case #%d: ",t);
        for(i=0;i<sz-N+1;++i)
        {
            if(s[i]=='-')
            {
                ++count;
                for(j=i;j<=i+N-1;++j)
                {
                    s[j] = (s[j]=='-') ? '+' : '-';
                }
            }
        }
        for(i=0;i<sz;++i)
        {
            if(s[i]=='-')
            {
                printf("IMPOSSIBLE\n");
                found = 1;
                break;
            }
        }
        if(found)
            continue;
        printf("%d\n",count);
    }
    return 0;
}
