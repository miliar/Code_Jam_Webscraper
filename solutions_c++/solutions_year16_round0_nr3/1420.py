#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

int n = 16, j = 50, q = 0;
ll v[50][11];

int primo(ll b, int ind)
{
    for(ll a = 2;a<=20;a++)
    {
        if(b%a==0)
        {
            v[q][ind] = a;
            return 1;
        }
    }
    return 0;
}

ll base(ll a, ll b)
{
    ll r = 0;
    ll m = 1;
    while(a!=0)
    {
        r+=(a%2)*m;
        a/=2;
        m*=b;
    }
    return r;
}

void chamada(ll a, int i)
{
    ll k;
    if(i<n && q<j)
    {
        chamada(a<<1, i+1);
        chamada((a<<1)+1, i+1);
    }
    else if(i==n && q<j)
    {
        if(a%2==1)
        {
            //printf("Valor %d\n", q);
            //printf("%llu\n", a);
            int s = primo(a, 2);
            for(k=3;k<=10;k++)
            {
                ll b = base(a, k);
                //printf("%llu\n", b);
                s+=primo(b, k);
            }
            //system("PAUSE");
            if(s==9)
            {
                int t;
                printf("%llu", base(a, 10));
                for(t=2;t<=10;t++)
                {
                    printf(" %llu", v[q][t]);
                }
                printf("\n");
                q++;
            }
        }
    }
}

int main()
{
    int t;
    cin>>t>>n>>j;
    cout<<"Case #1:\n";
    chamada(1, 1);
    return 0;
}
