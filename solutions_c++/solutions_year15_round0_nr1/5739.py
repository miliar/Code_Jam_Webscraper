#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("output1.out","w",stdout);
    ll t,p=0,n;
    scanf("%lld",&t);
    while(p<t)
    {
        p++;
        scanf("%lld",&n);
        ll a[n+5];
        char ch[n+5];
        scanf("%s",ch);
        //printf("%s",ch);
        ll ctr=0,cc=0;
        a[0]=(int)(ch[0]-48);
        ctr+=a[0];
        for(int i=1;i<=n;i++)
        {
            a[i]=(int)(ch[i]-48);
            //printf("::%d::\n",a[i]);
            if(ctr<i)
            {
                cc+=i-ctr;
                ctr+=(i-ctr);
            }
            ctr+=a[i];
        }
        printf("Case #%lld: %lld\n",p,cc);
    }
    fclose (stdout);
    fclose (stdin);

    return 0;
}
