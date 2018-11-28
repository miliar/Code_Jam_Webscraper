#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char ans[1005],s[1005];
void push_top (char c,int len)
{
    for(int i=len;i>0;i--)
        ans[i]=ans[i-1];
    ans[0]=c;

    return ;
}
void push_bottom (char c,int len)
{
    ans[len]=c;
    return ;
}
int main (void)
{
    int i,j,t,n;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%s",s);
        n=strlen(s);
        ans[0]=s[0];

        for(j=1;j<n;j++){
            if(s[j]>=ans[0])
                push_top(s[j],j);
            else
                push_bottom(s[j],j);
        }
        ans[n]='\0';
        printf("Case #%d: %s\n",i+1,ans);
    }

    return 0;
}
