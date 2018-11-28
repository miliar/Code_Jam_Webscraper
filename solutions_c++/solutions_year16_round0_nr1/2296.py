
#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

long long solve(long long n) {
    if ( n == 0 ) return -1;
    set<int> digits;
    for ( int i=1 ; true ; ++i ) {
        long long m = n * i;
        while ( m > 0 ) {
            digits.insert(m % 10);
            m /= 10;
        }
        if ( digits.size() == 10 ) return n * i;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for ( int tc=1 ; tc<=T ; ++tc ) {
        int n;
        scanf("%d", &n);
        long long res = solve(n);

        printf("Case #%d: ", tc);
        if ( res == -1 ) {
            printf("INSOMNIA\n");
        }
        else {
            printf("%lld\n", res);
        }
    }
    return 0;
}
