
#include <iostream>
#include <string>
#include <assert.h>

char helper(int x)
{
    switch( x ) {
        case 0:
            return '0';
        case 1:
            return '1';
        default:
            assert(false);
    }
    return 'p';
}

// a and b are considered as n-bit ints.
// output starts with 1, ends with 1, and in between it swaps back and forth taking bits from a vs b.
std::string buildResult(int a, int b, int n)
{
    std::string out;
    out.resize( n*2 + 2 );
    std::cerr << out.length();
    out[0] = '1';
    out[ out.length()-1 ] = '1';

    for ( int i = 0 ; i < n ; ++i ) {
        int slot = 1 + 2*i;
        out[ slot ]   = helper( (a>>i) & 1 );
        out[ slot+1 ] = helper( (b>>i) & 1 );
    }

    std::cerr<<out.length()<<std::endl;
    for ( int i = 0 ; i < 6 ; ++i )
        std::cerr<<out[i]<<std::endl;
    std::cerr<<out<<std::endl;
    return out;
}

int main()
{
    int T;
    std::cin >> T;
    assert( T == 1 );
    std::cout<<"Case #1:\n";

    int N;
    int J;
    std::cin >> N >> J;

    for ( int a = 0 ; a < J ; ++a ) {
        std::string result = buildResult( a , a , N/2 - 1 );
        std::cout << result;
        for ( int i = 3 ; i <= 11 ; ++i )
            std::cout << ' ' << i;
        std::cout << '\n';
    }

    return 0;
}
