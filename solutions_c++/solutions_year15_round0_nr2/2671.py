#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for( int tt=1; tt<=t; tt++ )
    {
        int d, p[1010];
        p[0] = 0;
        cin >> d;
        int maxp = 0;
        for( int i=1; i<=d; i++ )
        {
            cin >> p[i];
        }
        sort( p+1, p+d+1 );
        
        if( p[d] == 0 )
            printf("Case #%d: 0\n", tt);
        
        int lower=0, upper=p[d];
        while( lower < upper-1 )
        {
            int mid = (lower+upper)/2;
            // test
            int flag = 0;
            for( int i=0; i<mid; i++ )
            {
                int cur = min( d, i );
                int top = p[d-cur];
                int mintoeat = mid - i;
                
                if( top > mintoeat )
                    continue;
                int cnt = 0;
                for( int j=d-cur+1; j<d+1; j++ )
                    cnt += (p[j]-1)/mintoeat;
                if( cnt <= i )
                {
                    flag = 1;
                    break;
                }
            }
            if( flag == 1 )
                upper = mid;
            else lower = mid;
        }
        printf("Case #%d: %d\n", tt, upper);
    }
    return 0;
}