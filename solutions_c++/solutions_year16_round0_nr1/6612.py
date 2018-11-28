#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
//    freopen("A-large.in", "r", stdin);
//    freopen("o.txt", "w", stdout);
    ll t,test,n,i,temp;
    set <int> a;
    scanf("%lld",&test);
    for(t=1; t<=test; t++)
    {
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",t);
            continue;
        }
        for(i=1;;i++)
        {
            temp=n*i;
            while(temp!=0)
            {
                a.insert(temp%10);
                temp/=10;
            }
            if(a.size()==10)
                {
                    temp=n*i;
                    break;
                }
        }
        printf("Case #%lld: %lld\n",t,temp);
        a.clear();
    }
    return 0;
}
