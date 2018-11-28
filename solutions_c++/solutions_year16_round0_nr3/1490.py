/****************************************************/
/*                                                  */
/*  Fran Muñoz                                      */
/*  email: fran.mzy@gmail.com                       */
/*  UVA user: franmzy                               */
/*  Linkedin: https://www.linkedin.com/in/franmzy   */
/*                                                  */
/****************************************************/

#include <bits/stdc++.h>
using namespace std;

#define pb         push_back
#define mp         make_pair
#define LL         long long
#define ULL        unsigned long long
#define inf        1<<30
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)
#define DEBIN(n)   printf("GET IN: %d\n", n);
#define DEBOUT(n)   printf("GET OUT: %d\n", n);
#define UI          unsigned int

typedef pair<int, int> ii;
typedef vector<ii> vii;

#define MAX_LONG_PAN 500

int J, N;

ULL is_divisible (ULL num)
{
    if (num <=1)
        return 0;
    else if (num == 2)
        return 0;
    else if (num % 2 == 0)
        return 2;
    else
    {
        ULL divisor = 3;
        //long double num_d = static_cast<long double>(num);
        ULL upperLimit = static_cast<ULL>(sqrt(num) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                return divisor;
            divisor +=2;
        }
        return 0;
    }
}

ULL convert_to_base( ULL n, int base ){
    if( base == 2 ) return n;

    ULL number = 0;
    for( int i = N-1; i >= 0; i -- ){
        number*=base;
        number += ((n & (1 << i)) > 0) ? 1 : 0;
    }
    return number;
}

int main( int argc, char* argv[] )
{
    int n_cases;
    ULL nontrivial[12];
    bool is_jamcoin;
    int counter;

    scanf("%d\n", &n_cases);

    for( int i_case = 0; i_case < n_cases; i_case++ ) {
        scanf("%d %d", &N, &J);
        printf("Case #%d:\n", i_case+1);

        ULL start_jc = 1 << (N-1);
        start_jc += 1;
        ULL end_jc = 1 << N;

        counter = 0;
        for( ULL i_jc = start_jc; i_jc < end_jc && counter < J; i_jc+=2 ) {
            is_jamcoin = true;
            for( int base = 2; base <= 10; base++ ) {
                nontrivial[base] = is_divisible(convert_to_base(i_jc, base));
                if( !nontrivial[base] ) {
                    is_jamcoin = false;
                    break;
                }
            }
            if( is_jamcoin ){
                counter++;
                printf("%llu", convert_to_base(i_jc, 10));
                for( int base = 2; base <= 10; base++ ) {
                    printf(" %llu", nontrivial[base]);
                }
                printf("\n");
            }
        }
    }

    return 0;
}
