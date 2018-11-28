#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define pb push_back
#define sf scanf
#define pf printf
#define F first
#define S second
#define M 105
#define MOD 1e9+7

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    bool prove;
    int test;
    ll n, temp;

    bool arr[15];

    sf("%d", &test);
    for(int i=0; i<test; i++)
    {
        sf("%lld", &n);

        if(n==0)
        {
            pf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }

        for(int j=0; j<10; j++)
        {
            arr[j]=false;
        }

        ll mul=1;

        while(1)
        {
            temp=n*mul;
            while(temp)
            {
                arr[temp%10]=true;
                temp/=10;
            }

            prove=true;
            for(int j=0; j<10; j++)
            {
                if(!arr[j])
                {
                    prove=false;
                    break;
                }
            }

            if(prove)
            {
                break;
            }

            mul++;
        }

        pf("Case #%d: %lld\n", i+1, n*mul);
    }

    return 0;
}
