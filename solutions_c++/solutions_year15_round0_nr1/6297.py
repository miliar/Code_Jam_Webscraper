#include<bits/stdc++.h>
int main()
{
    int t,i,a[1005],j,k,l,p,q,m,n;
    char z,s[1005];
    freopen("q_a_1_l.txt","r",stdin);
    freopen("a_1_l.txt","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d",&n);
        p=0;
        scanf("%s",s);
        for(i=0;i<=n;i++)
        {
            a[i]=s[i]-'0';
        }
        n++;
        p=a[0];q=0;
        for(i=1;i<n;i++)
        {
            if(p<i)
            {
                q+=(i-p);
                p+=(i-p);
            }
            p+=a[i];
        }
        printf("Case #%d: %d\n",l,q);
    }
    return 0;
}
