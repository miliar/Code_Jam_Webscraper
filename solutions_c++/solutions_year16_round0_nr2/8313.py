#include <bits/stdc++.h>

#define lli long long int
#define fi first
#define se second
#define sc scanf
#define pr printf
#define pb push_back
#define mp make_pair
#define fin freopen( "input.txt", "r", stdin );
#define fout freopen( "output.txt", "w", stdout );

using namespace std;

int n, i, h;
string s;

int main()
{
    cin >> n;
    for( h = 1; h <= n; h++ ){
        cin >> s;
        char cur = '+';
        int cnt = 0;
        for( i = s.size() - 1; i >= 0; i-- ){
            if( s[i] != cur ){
                cnt++;
                cur = s[i];
            }
        }
        cout << "Case #" << h << ": " << cnt << endl;
    }
}
