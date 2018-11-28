#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,n;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    set <char> zed;
    char str[100];
    for(int i = 1; i <= t; i++)
    {
        scanf("%d",&n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        int k = n;
        while(true)
        {
            sprintf(str,"%d",n);
            for(int j = 0; str[j] != '\0'; j++)
            {
                zed.insert(str[j]);
            }
            if(zed.size() == 10)
                break;
            n+=k;
        }
        printf("Case #%d: %d\n",i,n);
        zed.clear();
    }
}
