#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A6.in","r",stdin);
    freopen("out5.txt","w",stdout);
    long long t,n,i,x,y,j;
    set<long long>a;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld",&n);
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",j);
        else
            {
        for(i=1;i>0;i++)
        {
            x=n*i;
            //cout<<x<<" ";
            while(x)
            {
                y=x%10;x=x/10;a.insert(y);
            }
            //cout<<a.size()<<endl;
            if(a.size()==10)
                break;
        }
        x=n*i;
        printf("Case #%lld: %lld\n",j,x);
            }
            a.clear();
    }
    return 0;
}
