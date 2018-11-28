#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;


int n;
char s[111];

int cal(int R)
{
    while(R>0&&s[R]=='+') R--;
    if(R<=0) return 0;

    int ans=0;

    if(s[1]=='+')
    {
        ans++;
        int l=1;
        while(l<=R&&s[l]=='+')
        {
            s[l]='-';
            l++;
        }
    }
    ans++;

    int ll=1,rr=R;

    while(ll<=rr&&s[ll]=='-') s[ll++]='+';

    while(ll<rr) swap(s[ll++],s[rr--]);
    return ans+cal(R);
}

void deal()
{
    scanf("%s",s+1);
    n=strlen(s+1);
    printf("%d\n",cal(n));
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        deal();
    }
    return 0;
}
