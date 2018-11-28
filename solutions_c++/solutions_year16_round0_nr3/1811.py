#include <iostream>
#include <stdio.h>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <time.h>
#include <cassert>
#include <map>
#include <set>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <bitset>


//#include <unordered_map>
//#include <unordered_set>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>
#define X first
#define Y second
#define endl "\n"
using namespace std;
const int MAXN = 3e5 + 7;
const int INF = 1e9 + 7;
const llong LINF = 1e18;
//const llong MOD = 1e9 + 7;
//const long double EPS = 1e-18;
using namespace std;
bool notprime[MAXN];
llong last = -1;
std::ostream&
operator<<( std::ostream& dest, __int128_t value )
{
    std::ostream::sentry s( dest );
    if ( s ) {
        __uint128_t tmp = value < 0 ? -value : value;
        char buffer[ 128 ];
        char* d = std::end( buffer );
        do
        {
            -- d;
            *d = "0123456789"[ tmp % 10 ];
            tmp /= 10;
        } while ( tmp != 0 );
        if ( value < 0 ) {
            -- d;
            *d = '-';
        }
        int len = std::end( buffer ) - d;
        if ( dest.rdbuf()->sputn( d, len ) != len ) {
            dest.setstate( std::ios_base::badbit );
        }
    }
    return dest;
}

bool isprime(__int128 x) {
    
    
    for (llong i = 2ll; i <= 1000000ll && i * i <= x; i++) {
        if (x % i == 0 ) {
            last = i;
            return false;
        }
    }
    return true;
}
string tostring(llong x) {
    string st;
    while (x)  {
        st += char(x % 2 + '0');
        x /= 2;
    }
    reverse(st.begin(), st.end());
    return st;
}
__int128 conv(string &st, int base) {
    __int128 res = 0;
    __int128 C = 1;
    for (int i = int(st.size()) - 1; i >= 0; i--) {
        res += (st[i] - '0') * C;
        C *= base;
    }
    return res;
}
int main() {
#ifdef DEBUG
    double beg = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);
#endif
    //ios_base::sync_with_stdio(0);cin.tie();
    int n = 32, J = 500;
   
    cout  << "Case #1:\n";
    for (llong i = (1ll << (n - 1)) + 1ll; ; i += 2ll) {
   
   
        bool good = true;
            string st = tostring(i);
        ;
            vector<llong> ans;
            for (int base = 2; base <= 10; base++) {
                if (isprime(conv(st, base))) {
                    good = false;
                    break;
                }
                ans.pb(last);
            }
            if (good) {
                cerr << J << '\n';
                cout << st << " ";
                J--;
                for (auto j: ans) {
                    cout << j << ' ';
                }
                cout << endl;
                if (!J) {
                    break;
                }
            }
        
    }
    
#ifdef DEBUG
    double end = clock();
    fprintf(stderr, "\n*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
#endif
    return 0;
}