#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define N 123456

int solve( int n )
{
        set < int > arr;
        int x = n;

        while( true )
        {
            int num = n;

            while( num )
            {
                arr.insert( num%10 );
                num /= 10;
            }
            if( arr.size()==10 )
                return n;
            n += x;
        }
        return n;
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for( int tt=1 ; tt<=t ; tt++ )
    {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",tt);
        (n==0)?puts("INSOMNIA"):printf("%d\n",solve(n));
    }

    return 0;
}

