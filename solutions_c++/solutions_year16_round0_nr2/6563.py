#include <stdio.h>
#include <iostream>
#include <string.h>

#define MAXN 105
using namespace std;

char S[MAXN];
int T;

int main()
{
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%s",S);
        printf("Case #%d: ",kase);
        int ans=0,L=strlen(S);
        char cur='+';
        for(int i=L-1;i>=0;i--)
        {
            if(cur!=S[i])ans++;
            cur=S[i];
        }
        printf("%d\n",ans);
    }
}
