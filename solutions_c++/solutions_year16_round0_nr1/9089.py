#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++)
    {
        set<int> s;
        ll n;
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",tc);
            continue;
        }
        ll mul=n;
        while(1)
        {
            ll temp=mul;
            while(temp)
            {
                s.insert(temp%10);
                temp/=10;
            }
            if(s.size()==10)
                break;
            mul+=n;
        }
        printf("Case #%d: %lld\n",tc,mul);
    }
    return 0;
}
