#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    
    scanf("%d", &t);
    
    for( int tt=1; tt<=t; tt++ )
    {
        int n;
        double ken[1010], naomi[1010];
        
        scanf("%d", &n);
        
        for( int i=0; i<n; i++ )
            scanf("%lf", &naomi[i]);
        sort( naomi, naomi+n );
        
        for( int j=0; j<n; j++ )
            scanf("%lf", &ken[j]);
        sort( ken, ken+n );
        
        int war=0, dwar=0, i, j=n-1;

        for( i=n-1; i>=0; i-- )
            if( ken[j] < naomi[i] )
                war++;
            else
                j--;
        
        j = 0;
        for(i=0; i<n; i++ )
            if( ken[j] < naomi[i] )
            {
                dwar++;
                j++;
            }
        
        printf("Case #%d: %d %d\n", tt, dwar, war);
    }
    
    return 0;
}