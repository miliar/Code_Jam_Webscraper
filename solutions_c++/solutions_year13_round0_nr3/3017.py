#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;
const int N = 1200;
int T, ans, a, b;
bool num[N];

bool judge( int x ) {
    string s, ss;
    bool is = true;
    while ( x ) {
        s += ( (x%10) + '0' );
        x /= 10;
    }
    //cout << s << endl;
    for ( int i = s.size()-1; i >= 0; --i ) ss += s[i];
    for ( int i = 0; i < s.size(); ++i ) if ( ss[i] != s[i] ) {
        is = false;
        break;
    }
    return is;
}
void init() {
    memset( num, 0, sizeof(num) );
    for ( int i = 1; i < 33; ++i ) {
        if( judge( i ) && judge( i*i ) ) num[i*i] = true;
    }
}
int main()
{
    freopen("s.in", "r", stdin);
    freopen("sp.txt", "w", stdout);

    init();
    scanf("%d", &T);
    int icase = 1;
    while ( T-- ) {
        scanf("%lld%lld", &a, &b);
        ans = 0;
        for ( int i = a; i <= b; ++i ) if ( num[i] ) ans++;
        printf("Case #%d: %d\n", icase++, ans); 
    }
}
