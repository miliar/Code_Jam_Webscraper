#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int i,j,a,b,n,m,t,Case=1;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        bool ok[11],yes;
        for(i=0;i<10;i++) ok[i]=false;
        for(i=1;i<=1000;i++)
        {
            yes=true;
            a=n*i;
            while(a>0){
                b=a%10;
                a/=10;
                ok[b]=true;
            }
            for(j=0;j<10;j++){
                if(ok[j]==false) yes=false;
            }
            if(yes) break;
        }
        if(yes) printf("Case #%lld: %lld\n",Case++,i*n);
        else printf("Case #%lld: INSOMNIA\n",Case++);
    }
    return 0;
}
