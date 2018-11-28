#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int t;
int n;
char str[200111];

inline int MAX(int a,int b)
{
    if (a>b)
    return a;
    else
    return b;
}

inline int Calc(int a,int b)
{
    if (str[a]==str[b])
    return 10;
    else
    return 5;
}

char s[200111];
int sL=0;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int test;
    int i,j;
    int ind;
    int ans=0;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        ans=0;

        fprintf(stderr,"Starting test #%d\n",test);

        scanf("%s",str+1);
        n=strlen(str+1);

        sL=0;
        for (i=1;i<=n;i++)
        {
            if (sL==0)
            {
                sL++;
                s[sL]=str[i];
            }
            else
            {
                if (s[sL]==str[i])
                {
                    sL--;
                    ans+=10;
                }
                else
                {
                    sL++;
                    s[sL]=str[i];
                }
            }
        }

        ans+=(sL/2)*5;

        printf("Case #%d: %d\n",test,ans);
    }

    return 0;
}
