#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
map < int , int > mp;
int sum = 0;
void check(ull p)
{
    while( p > 0 )
    {
        ull a = p % 10;
        p = p / 10;
        if( !mp[a] )
        {
            mp[a]++;
            sum++;
        }
    }

}
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin >> t;
    for( int k = 1; k <= t; k++ )
    {
        mp.clear();
        sum = 0;
        ull n, ans;
        cin >> n;
        cout << "Case #" << k << ": ";
        if( n == 0 )
        {
            cout << "INSOMNIA\n";
            continue;
        }
        ans = n;
        check( ans );
        for( int i = 2;  ; i++ )
        {
            if( sum == 10 ) break;
            ans = i * n;
            check( ans );

        }
        cout << ans << "\n";
    }
}
