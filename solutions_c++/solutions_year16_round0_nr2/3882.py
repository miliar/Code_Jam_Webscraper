#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char s[105];
FILE*out;
void solve2 (void)
{
    int i,n,t,len=0;
    char tmp[105]={0,};

    n=strlen(s);

    tmp[len++]=s[0];
    t=s[0]=='-'?1:0;
    for(i=1;i<n;i++)
        if(s[i-1]!=s[i]) tmp[len++]=s[i];

    fprintf(out,"%d\n",len-(len%2+t)%2);
    return ;
}
int main (void)
{
    int i,t;

    freopen("input.txt","r",stdin);
    out=fopen("output.txt","w");

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%s",s);
        fprintf(out,"Case #%d: ",i+1);
        solve2();
    }

    return 0;
}
