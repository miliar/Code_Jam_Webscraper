#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

ll factors[20];
int bits[20];
int cnt;
int n;

bool check(int base)
{
    ll x=0;
    for (int i=0;i<n;i++)
        x=x*base+bits[i];
    for (int i=2;(ll)i*i<=x;i++)
    {
        if (x%i==0)
        {
            factors[base]=i;
            return true;
        }
    }
    return false;
}
void solve(int step)
{
    if(cnt>=50)
        return;
    if(step==n-1)
    {
        bool isok=true;
        for (int base=2;base<=10;base++)
        {
            if(!check(base))
            {
                isok=false;
                break;
            }
        }
        if (isok)
        {
            for(int i=0;i<n;i++)
                printf("%d",bits[i]);
            for(int i=2;i<=10;i++)
                printf(" %d",factors[i]);
            printf("\n");
            cnt++;
        }
        return;
    }
    bits[step]=0;
    solve(step+1);
    bits[step]=1;
    solve(step+1);
}

int main()
{
    //freopen("C:\\Users\\lpc\\Downloads\\")
    freopen("e:\\codejam\\3.txt","w",stdout);
    printf("Case #1:\n");
    n = 16;
    bits[0]=bits[15]=1;
    solve(1);
    return 0;
}