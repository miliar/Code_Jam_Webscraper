#include <cstdio>

using namespace std;

double sol, Wait, Buy, Production, C, F, X;
int T, K;

int main ( void ) {
    scanf ( "%d", &T );
    K = T;
    while ( K-- ) {
        Production = 2;
        sol = 0;
        scanf ( "%lf %lf %lf", &C, &F, &X );
        while ( true ) {
            Wait = X / Production;
            Buy = C / Production + ( X / ( Production + F ) );
            //printf ( "%lf %lf\n", Wait, Production );
            if ( Wait <= Buy ) {
                sol += Wait;
                break;
            } else {
                sol += C / Production;
                Production += F;
            }
        }
        printf ( "Case #%d: %.7lf\n", T - K, sol );
    }
    return 0;
}
