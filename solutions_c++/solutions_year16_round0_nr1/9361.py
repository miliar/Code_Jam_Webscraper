#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for( int tt=1; tt<=t; tt++ )
    {
        long long int n, end;
        cin >> n;
        end = n*10000;
        int seen = 0;
        
        for( long long int sum=n; sum<end; sum+=n )
        {
            long long int cur = sum;
            while( cur )
            {
                int d = cur%10;
                cur /= 10;
                seen = seen | (1<<d);
            }
            
            if( seen == 0x3FF )
            {
                if( n==90 )
                printf("Case #%d: %lld\n", tt, sum);
                break;
            }
        }
        
        if( seen != 0x3FF )
            printf("Case #%d: INSOMNIA\n", tt);
    }
    
    return 0;
}
