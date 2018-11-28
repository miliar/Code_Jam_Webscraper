#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[105];
int n;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,m;
    int total,cas=0,ans;
    cin >> t;
    while(t--)
    {
        scanf("%s%d",s,&n);
        int l = strlen(s);
        ans = 0;
        printf("Case #%d: ",++cas);
        for(i=0;i<l;i++)
        for(m=total=0,j=i;j<l;j++)
        {
            if(s[j]!='a'&&s[j]!='e'&&s[j]!='i'
               &&s[j]!='o'&&s[j]!='u')
               total++,m=max(total,m);
            else
            total = 0;
            if(m>=n)
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
