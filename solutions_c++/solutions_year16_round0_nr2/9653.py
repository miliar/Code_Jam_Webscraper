#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

int solve( string& S )
{
    int N = S.length();
    int l = 0, r = N-1;
    int steps = 0;
    while( 1 )
    {
        l = 0;
        while( r >= 0 && S[r] == '+' )
            r--;
        if( r < 0 )
            break;
        if( S[l] == '+' )
        {
            while( l <= r && S[l] == '+' )
                l++;
            for( int i = 0; i < l; i++ )
                S[i] = '-';
            steps++;
        }
        for( int i = 0; i <= r; i++ )
            swap(S[i], S[r-i]);
        for( int i = 0; i <= r; i++ )
            if( S[i] == '+' )
                S[i] = '-';
            else
                S[i] = '+';
        steps++;
    }
    return steps;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int c = 1;
    string S;
    while( c <= T )
    {
        cin >> S;
        int steps = solve(S);
        printf("Case #%d: %d\n", c, steps);
        c++;
    }
    return 0;
}
