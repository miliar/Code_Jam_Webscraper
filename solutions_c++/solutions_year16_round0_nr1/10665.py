#include<bits/stdc++.h>
using namespace std;
#define ll long long
int t;
ll n;

vector<ll> v;

void bsearch(ll rem)
{
    ll a,b;
    int flag=1;

    if(v.empty())
        v.push_back(rem);
    else
    {
        a=0,b=v.size()-1;

        while(a <= b)
        {
            ll mid = (a + (b-a)/2);

            if(v[mid] == rem)
            {
                flag=0;
                break;
            }
            else if(v[mid] > rem)
                b = mid-1;
            else
                a = mid+1;
        }

        if(flag)
        {
            if(a >= v.size())
                v.push_back(rem);
            else
                v.insert(v.begin()+a,rem);
        }
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    scanf("%d",&t);

    for(int k=1;k<=t;++k)
    {
        v.clear();

        scanf("%lld",&n);
        ll i=1;
        int flag=1;

        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",k);
            continue;
        }

        while(flag)
        {
            ll a = i*n;

            while(a>0)
            {
                ll rem = a%10;
                a /= 10;

                bsearch(rem);
            }

            if(v.size()==10)
                flag=0;
            ++i;
        }

        printf("Case #%d: %lld\n",k,(i-1)*n);
    }
    return 0;
}
