#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char s[1<<8];
int n;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int c,t,i,k;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%s",&s[1]);
        n=strlen(&s[1]);
        for(i=n;i>=1;i--)
        {
            if(s[i]=='-')
            {
                break;
            }
        }
        for(k=0;i>=1;i--)
        {
            if(s[i]!=s[i-1])
            {
                k++;
            }
        }
        printf("Case #%d: %d\n",c+1,k);
    }
    return 0;
}
