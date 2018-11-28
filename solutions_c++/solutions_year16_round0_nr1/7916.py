#include <bits/stdc++.h>
#define N       10
using namespace std;

bool seen[N];

int main() {
    freopen( "A-large.in", "rt", stdin );
    freopen( "output.txt", "wt", stdout );
    int T, cases = 0;
    cin >> T;

    while ( T-- ){
        int n, cont = 0, i = 1;
        long long number, res;
        cin >> n;

        memset( seen, 0, sizeof seen );

        if( n == 0 ){
            cout << "Case #" << ++cases << ": INSOMNIA\n";
            continue;
        }

        while( cont < 10 ){
            number = (long long)i++ * n;
            while( number > 0 ){
                res = number % 10;
                number /= 10;
                if( !seen[res] ){
                    seen[res] = 1;
                    ++cont;
                }
            }
        }

        cout << "Case #" << ++cases << ": " << (i - 1) * n << '\n';
    }
}
