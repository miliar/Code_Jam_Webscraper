#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int T,co,n;
    bool check[10];
    scanf("%d",&T);
    for ( int test=1 ; test<=T ; test++ )
    {
        scanf("%d",&n);
        for ( int c=0 ; c<10 ; c++ )    check[c] = false;
        co = 0;
        if ( n == 0 )   printf("Case #%d: INSOMNIA\n",test);
        else
        {
            for ( long long c=n ;  ; c+=n )
            {
                long long temp = c;
                while ( temp != 0 )
                {
                    if ( !check[temp%10] )
                    {
                        check[temp%10] = true;
                        co++;
                    }
                    temp = temp/10;
                }
                if ( co == 10 )
                {
                    printf("Case #%d: %lld\n",test,c);
                    break;
                }
            }
        }
    }
}
