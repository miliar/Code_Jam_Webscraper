#include <bits/stdc++.h>
using namespace std;
bool digit[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cas,x;
    scanf("%d",&cas);
    for (int run=1;run<=cas;++run)
    {
        scanf("%d",&x);
        printf("Case #%d: ",run);
        if (x==0)
            puts("INSOMNIA");
        else
        {
            memset(digit,0,sizeof digit);
            int cnt=10,cur=0;
            while (cnt)
            {
                cur+=x;
                for (int t=cur;t;t/=10)
                    if (!digit[t%10])
                    {
                        digit[t%10]=true;
                        --cnt;
                    }
            }
            printf("%d\n",cur);
        }
    }
    return 0;
}
