#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t, n, i, j, x, l, f;
    scanf("%d", &t);
    for(l=1; l<=t; l++)
    {
        x=0; f=0;
        char s[1000], c;
        scanf(" %s", s);
        n =strlen(s);
        c = s[0];
        for(i=1; i<n; i++)
        {
            if(s[i]!=c)
            {
                x++;
                c = s[i];
            }
        }
        if(c=='-')
            x++;
        printf("Case #%d: %d\n", l, x);
        c=0;
    }
    return 0;
}
