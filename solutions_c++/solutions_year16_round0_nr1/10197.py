#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>

using namespace std;
typedef long long int ll;
ll COUNTED_DIGIT[10];
ll count = 0;
void initialize();
bool reflaxArray(ll n);

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    ll t, n, x, y;
    cin >> t;
    for(x=1; x<=t; x++)
    {
        initialize();
        cin >> n;
        printf("Case #%lld: ", x);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        for(ll i=1;;i++)
        {
            if(reflaxArray(i*n))
            {
                printf("%lld\n", i*n);
                break;
            }
        }

    }
    return 0;
}
void initialize()
{
    for(int i=0; i<10; i++)
    {
        COUNTED_DIGIT[i]=0;
    }
    count=0;
}
bool reflaxArray(ll n)
{
    ll lastDigit;
    while(n)
    {
        lastDigit = n%10;
        if(COUNTED_DIGIT[lastDigit]==0)
        {
            COUNTED_DIGIT[lastDigit] = 1;
            count++;
        }
        if(count==10) return true;
        n/=10;
    }
    return false;
}
