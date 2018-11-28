#include <bits/stdc++.h>

using namespace std;

char s[202], s2[202];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt","w", stdout);
    int t,cnt, cs=1;
    scanf("%d",&t);

    while(t--)
    {
        cnt=0;
        scanf("%s",s);

        printf("Case #%d: ", cs++);

        int n= strlen(s);

        for(int i=1; i<n; i++)
        {
            if(s[i]!=s[i-1]) cnt++;
        }
        if(s[n-1]=='-') cnt++;
        printf("%d\n",cnt);
    }
}
