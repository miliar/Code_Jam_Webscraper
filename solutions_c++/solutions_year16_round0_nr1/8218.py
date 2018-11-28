//Coded by: speeDemon/thunderclash
#include<bits/stdc++.h>
#define dbg(x)
using namespace std;
typedef long long ll;

int main()
{
    freopen("Ain2.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    ll t,n;
    ll i,tinit;
    ll mul,d,tmp;
    ll digits[10];
    cin>>t;
    tinit = t;
    while(t--)
    {
        cin>>n;
        if(n==0){
            printf("Case #%lld: INSOMNIA\n",tinit-t);
            continue;
        }

        for(i=0;i<=9;++i)
            digits[i]=0;
        mul = 0;
        for(i=1;;++i)
        {
            mul += n;
            tmp = mul;
            while(tmp)
            {
                d = tmp%10;
                digits[d]=1;
                tmp/=10;
            }
            for(i=0;i<=9;++i)
                if(digits[i]==0)
                    break;
            if(i==10)
            {
                printf("Case #%lld: %lld\n",tinit-t,mul);
                break;
            }
        }
    }
    return 0;
}
