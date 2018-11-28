#include <stdio.h>
using namespace std;

long long int n;
void solve()
{

    scanf("%lld",&n); 
    long long int nn = 0;
    int digs[10];
    for (int i=0;i<10;i++) digs[i] = 0;
    int count = 0;
    for (long long int i=0;i<=1000001;i++)
    {
        nn += n; 
        long long int m = nn ;
        while ( m > 0 )
        {
            if ( digs[m % 10] == 0 ) 
            {
                digs[m %10] = 1;
                count++;
            }
            m = m/10;
        }
        if ( count == 10 ) { printf("%lld\n",nn);  return;}; 
    }


    printf("INSOMNIA\n");
}

int main()
{
    int T;
    printf("\n");
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
