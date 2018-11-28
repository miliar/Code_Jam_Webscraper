#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <unordered_map>
#define log(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long ll;
typedef pair<int, int> ip;
typedef pair<ll, ll> lp;

int T, N;
int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++ ) {
        scanf("%d", &N);
        vector<ip> v;
        int tot = 0;
        for ( int i = 0; i < N; i++ ) {
            int x;
            cin >> x;
            v.push_back(ip(x, i));
            tot += x;
        }
        printf("Case #%d:", t);
        while ( tot > 0 ) {
            sort(v.begin(), v.end());
            reverse(v.begin(), v.end());
            if ( v[0].first == 0 ) break;
            bool f = false;
            for ( int i = 2; i > 0; i-- ) {
                for ( int j = 1; j >= 0; j-- ) {
                    if ( i == 2 && j > 0 ) continue;
                    if ( v[0].first < i || v[1].first < j ) continue;
                    int x = v[0].first - i;
                    int y = v[1].first - j;
                    int nt = tot - i - j;
                    bool cant = false;
                    for ( int i = 2; i < N; i++ ) if ( v[i].first * 2 > nt ) {
                        cant = true;
                        break;
                    }
                    if ( cant ) continue;
                    if ( 2 * x <= nt && 2 * y <= nt ) {
                        f = true;
                        printf(" ");
                        for ( int k = 0; k < i; k++ ) printf("%c", v[0].second + 'A');
                        for ( int k = 0; k < j; k++ ) printf("%c", v[1].second + 'A');
                        tot = nt;
                        v[0].first -= i;
                        v[1].first -= j;
                        break;
                    }
                }
                if ( f ) break;
            }
        }
        putchar('\n');
    }
    return 0;
}
