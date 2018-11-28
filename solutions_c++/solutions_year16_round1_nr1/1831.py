#include<bits/stdc++.h>
using namespace std;
char in[1005],ans[4000];
int main()
{
    //freopen("A small input.in","r",stdin);
    //freopen("A small output.out","w",stdout);
    freopen("A large input.in","r",stdin);
    freopen("A large output.out","w",stdout);
    int t,ti,m,n,i,j,k,l,a=1500,b=1500;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        printf("Case #%d: ",ti);
        a=b=1500;
        scanf("%s",in);
        l=strlen(in);
        ans[a]=in[0];
        b++;
        for(j=1;j<l;j++)
        {
            if(in[j]>=ans[a])
                ans[--a]=in[j];
            else
                ans[b++]=in[j];
        }
        for(j=a;j<b;j++)
            printf("%c",ans[j]);
        printf("\n");
    }
}
