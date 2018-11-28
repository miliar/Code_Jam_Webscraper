#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("armaanin1l.txt","r",stdin);
    freopen("armaan1l.txt","w",stdout);
    int i,j,k,n,t,ans,p;
    char s[1010],ch;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        ans=0;
        scanf("%d",&k);
        scanf("%s",s);
        ch=getchar();
        p=s[0]-'0';
        for(i=1;i<=k;i++)
        {
            ans=max(ans,(i-p));
            p+=s[i]-'0';
        }
        printf("Case #%d: %d\n",j,ans);
    }
}
