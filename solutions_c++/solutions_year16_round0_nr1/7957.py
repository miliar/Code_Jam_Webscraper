#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main ()
{
    freopen("A_large.in", "r", stdin);
	freopen("A_large.out","w",stdout);
    ll cases,caseno=0,num,i;
    scanf("%lld",&cases);

    while(cases--)
    {
        scanf("%lld",&num);
        if (num==0)
        {
            printf("Case #%lld: INSOMNIA\n",++caseno);
            continue;
        }
        ll temp;
        set<ll>data;
        for (i=1;;i++)
        {
            temp=num*i;
            while(temp!=0)
            {
                data.insert(temp%10);
                temp/=10;
            }
            if (data.size()==10)
                break;
        }
        printf("Case #%lld: %lld\n",++caseno,num*i);
    }
    return 0;
}
