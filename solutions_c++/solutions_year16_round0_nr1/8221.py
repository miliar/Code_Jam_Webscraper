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

bool used[10];

lli f( lli x )
{
    while( x ){
        used[x % 10] = true;
        x /= 10;
    }
}

int main()
{
    lli i, j, h, n, x, cnt;
    cin >> n;
    for( h = 1; h <= n; h++ ){
        cin >> x;
        cnt = 0;
        for( i = 1; i <= 10000; i++ ){
            f(x * i);
            bool b1 = true;
            for( j = 0; j < 10; j++ )
                if( used[j] == false )
                    b1 = false;
            if( b1 )
                break;
        }
        cout << "Case #" << h << ": ";
        if( i == 10001 )
            cout << "INSOMNIA" << endl;
        else
            cout << x * i << endl;
        for( i = 0; i < 10; i++ )
            used[i] = false;
    }
}
