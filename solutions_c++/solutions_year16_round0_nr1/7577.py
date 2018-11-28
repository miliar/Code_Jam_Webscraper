#include <cstdio>
#include <iostream>
#define INT long long int
using namespace std;
int t;

bool done(bool *chk)
{
    for(int i = 0 ; i < 10 ; i++ )
        if( !chk[i] ) return false;
    return true;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("res.txt","w",stdout);
    scanf("%d", &t);
    for(int i = 1 ; i <= t ; i++ )
    {
        bool chk[10] = {0};
        INT n, pre, m, ans = 0;
        scanf("%lld", &n), pre = n;
        
        if( n == 0 ) printf("Case #%d: INSOMNIA\n", i);
        else
        {
            
        while(1)
        {
            m = pre;
            while(m)
            {
                chk[m%10] = true;
                m/=10;
            }
            ans++, pre+=n;
            if( done(chk) ) break;
        }
        printf("Case #%d: %lld\n", i, pre-n);
        }
        
    }
}