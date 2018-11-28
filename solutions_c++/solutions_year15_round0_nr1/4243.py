#include<iostream>
#include<cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,l,ca,c,ans;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
    {
        char s[1010];
        scanf("%d %s",&l,&s);
        c=0;
        ans=0;
        for(i=0;i<=l;i++)
        {
            if(i<=c)
            {
                c+=(s[i]-'0');
            }
            else
            {
                c++;
                ans++;
                c+=(s[i]-'0');
            }
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
