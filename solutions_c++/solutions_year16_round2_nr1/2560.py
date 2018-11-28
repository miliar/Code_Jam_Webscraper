#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int cnt[27], ans[10];
const int N = 2010;

vector < string > query, T;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, i, j, k, num, currNum;
    string s;
    cin >> t;
    for ( i = 1; i <= t; i++ ){
        cin >> s;
        query.push_back(s);
    }
    for ( i = 0; i <= 9; i++ ){
        cin >> s;
        T.push_back(s);
    }
    for ( i = 0; i < t; i++ ){
        s = query[i];
        for ( j = 0; j < 10; j++ ){
            ans[j] = 0;
        }
        for ( j = 1; j <= 26; j++ ){
            cnt[j] = 0;
        }
        for ( j = 0; j < size(s); j++ ){
            cnt[ s[j] - 'A' ]++;
        }

        for ( j = 0; j <= 9; j++ ){
            num = tolower( T[j][0] ) - 'a';
            for ( k = 1; k < size( T[j] ) - 1; k++ ){
                currNum = tolower( T[j][k] ) - 'a';
                if ( currNum == num ){
                    continue;
                }
                cnt[ currNum ] -= cnt[ num ];
            }
            ans[ T[j][ size(T[j]) - 1 ] - '0' ] = cnt[num];
            cnt[num] = 0;
        }
        cout << "Case #" << i + 1 << ": ";
        for ( j = 0; j <= 9; j++ ){
            for ( k = 1; k <= ans[j]; k++ ){
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}
