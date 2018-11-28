#include <bits/stdc++.h>

using namespace std;

int main()
{
    int cases,k=1;
    scanf( "%d",&cases );
    char A[1500];
    while( cases-- )
    {
        int smax;
        scanf( "%d",&smax );
        scanf( "%s",A );
        long long preSum = 0,res = 0;
        preSum += (A[0]-'0');   
        for( int i=1;i<=smax;i++ )
        {
            if( preSum < i )
            {
                res += abs(i-preSum);
                preSum += abs(i-preSum);

            }
            preSum += (A[i]-'0');
        }
        printf( "Case #%d: %lld\n",k,res );
        k++;
    }
    return 0;
}
