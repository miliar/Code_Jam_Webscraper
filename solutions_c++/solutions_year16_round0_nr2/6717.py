#include <bits/stdc++.h>
using namespace std;
int main()
{
        //freopen("B-large.in", "r", stdin);
        //freopen("OB.txt", "w", stdout);

    char a[400];
    int t, i, j, ans;
    scanf("%d", &t);
    for(i=0; i<t; i++)
    {

        ans=0;
        scanf(" %s", a);
        for(j=1; j<strlen(a); j++)
        {
            if(a[j]!=a[j-1])
                ans++;
        }
        if(a[strlen(a)-1]=='-')
            ans++;
        printf("Case #%d: %d\n", i+1, ans);
    }
    return 0;
}
