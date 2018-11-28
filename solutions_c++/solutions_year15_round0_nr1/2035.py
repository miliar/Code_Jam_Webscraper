#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a-large_out.txt","w",stdout);
    int cas,n;
    char s[1500];
    scanf("%d",&cas);
    for (int c=1; c<=cas; c++)
    {
        scanf("%d%s",&n,s);
        int tot=1,need=0;
        for (int i=0; i<=n; i++)
        {
            //cout<<i+1<<"   "<<tot<<endl;
            if (i+1<=tot)
            {
                tot+=s[i]-'0';
            }
            else
            {
                need=max(i+1-tot,need);
                tot+=s[i]-'0';
            }
        }

        printf("Case #%d: %d\n",c,need);
    }
    return 0;
}
