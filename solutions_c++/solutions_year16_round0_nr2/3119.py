#include <bits/stdc++.h>
using namespace std;
int nrt,l,i,sol,nr,t,n;
char s[200];
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d\n",&nrt);
    for(l=1;l<=nrt;l++)
    {
        gets(s);
        n=strlen(s);
        sol=0;
            t=0;
            nr=0;
            for(i=0;i<n;i++)
            {
                if(s[i]==s[i+1])t++;
                else
                {
                    nr++;
                }
            }
            if(s[n-1]=='+')nr--;
        sol=nr;
        printf("Case #%d: ",l);
        printf("%d\n",sol);
    }
    return 0;
}
