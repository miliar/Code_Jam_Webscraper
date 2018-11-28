#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define N 100010
#define LN 17
#define mod (int)(1e9+7)

double dp[LN][LN];
double arr[LN];

double solve( int num , int rem )
{
    if( num==0 ) {
        if( rem!=0.0 ) return 0;
        return 1.0;
    }

    if( rem == 0 )
        return dp[num][rem] = (1 - arr[num])*solve( num-1, rem );

    if( dp[num][rem]!=-1.0 )
        return dp[num][rem];

    dp[num][rem] = ( arr[num] )*solve( num-1 , rem-1)+ ( 1 - arr[num])*solve( num-1, rem );
    //printf("%.6lf %d %d %.6lf\n",dp[num][rem],num,rem,arr[num]);
    return dp[num][rem];
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int T;
    scanf("%d",&T);

    for( int cases=1; cases <= T; cases++ )
    {
        printf("Case #%d: ",cases);
        int n,K ; scanf("%d %d",&n,&K);

        double prob[n];

        for( int i = 0 ; i< n ; i++ )
        {
            scanf("%lf",&prob[i]);
            //printf("%d %.6lf---->\n",i,prob[i]);
        }

        double ans = 0;
        int ways = 0;
        for( int i = 0; i<(1<<n) ; i++ )
        {
            int counter = 0;
            for( int j=0; j<n ; j++ )
            {
                if( (i&(1<<j)))
                {
                    counter++;
                    arr[counter]=prob[j];
                    //printf("%d %.6lf----\n",counter,prob[j]);
                }
            }
            if( counter==K ) {
                for( int j = 0; j<LN ; j++ )
                    for( int k = 0; k<LN ; k++ )
                     dp[j][k]=-1;
                ways ++ ;
                ans = max( ans, solve( counter,K/2));
            }

        }
        printf("%.6lf\n",ans);
    }
	return 0;
}


