#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int go ( vector<int> a ) {
    int best = 2000000000;
    for ( int i = 0; i < a.size(); i++ ) {
        int curr = 0;
        for ( int j = 0; j < a.size(); j++ ) {
            if ( i != j ) {
                curr += abs(a[i]-a[j]);
            }
        }
        best = min(best, curr);
    }
    return best;
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; scanf( "%d", &tc );
    for ( int _ = 0; _ < tc; _++ ) {
        printf( "Case #%d: ", _+1 );
        int n; scanf( "%d\n", &n );
        string s[105];
        int a[105][105];
        char c[105];
        int nn = 0;
        bool good = true;
        for ( int i = 0; i < n; i++ ) {
            cin >> s[i];

            char last = s[i][0];
            int ind = 0;
            int cnt = 1;
            
            if ( !i ) {
                for ( int j = 1; j < s[i].length(); j++ ) {
                    if ( s[i][j] != last ) {
                        c[ind] = last;
                        a[i][ind] = cnt;
                        cnt = 1;
                        ind++;
                    }
                    else {
                        cnt++;
                    }
                    last = s[i][j];
                }
                a[i][ind] = cnt;
                c[ind] = last;
                nn = ind + 1;
            }
            else {
                for ( int j = 1; j < s[i].length(); j++ ) {
                    if ( s[i][j] != last ) {
                        if ( last != c[ind] ) {
                            good = false;
                            break;
                        }
                        a[i][ind] = cnt;
                        cnt = 1;
                        ind++;
                    }
                    else {
                        cnt++;
                    }
                    last = s[i][j];
                }
                if ( ind+1 != nn ) {
                    good = false;
                }
                if ( last != c[ind] ) {
                    good = false;
                }
                a[i][ind] = cnt;
            }
            if ( !good ) break;
        }

        if ( !good ) {
            printf( "Fegla Won" );
        }
        else {
            int res = 0;
            for ( int i = 0; i < nn; i++ ) {
                vector<int> arg;
                for ( int j = 0; j < n; j++ ) {
                    arg.push_back(a[j][i]);
                }
                res += go(arg);
            }
            printf( "%d", res );
        }
        
        printf( "\n" );
    }
    
    return 0;
}
