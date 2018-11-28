#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define ll long long
int GCD(int a, int b)
{
    return b? GCD(b,a%b) : a;
}
long long prim(long long n)
{
    long long num,i;
    num=n;
    for(i=2; i*i<=n; i++)
    {
        if(num%i==0)
        {
            while(num%i==0)
            {
                num/=i;
            }
        }
    }
    if(num==n)
        return 1;
    else
        return 0;
}
long long chhotu(long long n)
{
    long long num,i;
    num=n;
    for(i=2; i*i<=n; i++)
    {
        if(num%i==0)
        {
            break;
        }
    }
    return i;
}
long long POW(long long Base, long long Exp)
{
    long long y,ret=1;
    y=Base;
    while(Exp)
    {
        if(Exp&1)
            ret=(ret*y);
        y = (y*y);
        Exp/=2;
    }
    return ret;
}
long long int modular_pow(long long int base, int exponent,
                          long long int modulus)
{
    long long int result = 1;

    while (exponent > 0)
    {
        if (exponent & 1)
            result = (result * base) % modulus;

        exponent = exponent >> 1;

        base = (base * base) % modulus;
    }
    return result;
}

long long int PollardRho(long long int n)
{
    srand (time(NULL));

    if (n==1) return n;

    if (n % 2 == 0) return 2;

    long long int x = (rand()%(n-2))+2;
    long long int y = x;

    long long int c = (rand()%(n-1))+1;

    long long int d = 1;

    while (d==1)
    {
        x = (modular_pow(x, 2, n) + c + n)%n;

        y = (modular_pow(y, 2, n) + c + n)%n;
        y = (modular_pow(y, 2, n) + c + n)%n;

        d = __gcd(abs(x-y), n);

        if (d==n) return PollardRho(n);
    }

    return d;
}
int main()
{
    int t,tc;
    cin>>t;
    for(tc=1; tc<=t; tc++)
    {
        int k,c,s,i;
        cin>>k>>c>>s;

        printf("Case #%d: ",tc);
        for(i=1; i<=k; i++)
            		printf("%d ",i);
        cout<<endl;
    }
    return 0;
}
