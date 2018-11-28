#include<cstdio>

int main( void ){
    int T;
    long long r, t;
    int count;

    scanf("%d", &T);

    for ( int i = 0 ; i < T ; ++i ){
        scanf("%lld %lld", &r, &t);
        count = 0;
        for ( long long j = r + 1; ; j += 2 ){
            t -= ( 2 * j - 1 );
            if ( t >= 0 )
                ++count;
            else
                break;
        }
        printf("Case #%d: %d\n", i + 1, count);
    }
    return 0;
}
