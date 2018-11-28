#include <bits/stdc++.h>
using namespace std;
char str[107];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int run=1;run<=cas;++run)
    {
        scanf("%s",str);
        printf("Case #%d: ",run);
        int ans=1;
        for (int i=1;str[i];++i)
            if (str[i]!=str[i-1])
                ++ans;
        if (str[strlen(str)-1]=='+') --ans;
        printf("%d\n",ans);
    }
    return 0;
}
