#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

char s[1<<10];
string m;
int n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%s",s);
        n=strlen(s);
        m="";
        for(i=0;i<n;i++)
        {
            m=max(s[i]+m,m+s[i]);
        }
        printf("Case #%d: %s\n",c+1,m.c_str());
    }
    return 0;
}
