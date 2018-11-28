#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int a[1010];
char s[1010];

int main()
{
//ÎÄ¼þ²Ù×÷
//    freopen("A-small-attempt2.in", "r", stdin);
//    freopen("A-small-attempt2.out", "w", stdout);

//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);


    int T;
    cin >> T;

    for ( int caes = 1; caes <= T ; ++ caes) {
        int n, ans = 0, temp = 0;
        cin >> n;
        memset( a, 0, sizeof( a) );
        cin >> s;

        for ( int i = 0; i <= n; ++ i) {
            a[i] = s[i] - '0';
        }

        for ( int i = 1; i <= n; ++ i) {
            temp += a[ i - 1];
            if ( a[i] && i > temp) {
                ans += i - temp;
                temp += i - temp;
            }
        }

        cout << "Case #" << caes << ": " << ans << endl;
    }


    return 0;
}
