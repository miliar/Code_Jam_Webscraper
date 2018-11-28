#include <iostream>
#include <cstdio>
using namespace std;
const int superConst = 13;

struct element
{
    int sgn;
    char sym;
    element(){}
    element( int _sgn , char _sym )
    {
        sgn = _sgn;
        sym = _sym;
    }
};

element operator *( element a , element b )
{
    int newSgn = a.sgn * b.sgn;
    if ( a.sym == 'a' ) return element( newSgn , b.sym );
    if ( b.sym == 'a' ) return element( newSgn , a.sym );
    if ( a.sym == b.sym ) return element( (-1) * newSgn , 'a' );
    if ( a.sym == 'i' && b.sym == 'j' ) return element(        newSgn , 'k' );
    if ( a.sym == 'j' && b.sym == 'i' ) return element( (-1) * newSgn , 'k' );
    if ( a.sym == 'j' && b.sym == 'k' ) return element(        newSgn , 'i' );
    if ( a.sym == 'k' && b.sym == 'j' ) return element( (-1) * newSgn , 'i' );
    if ( a.sym == 'k' && b.sym == 'i' ) return element(        newSgn , 'j' );
    if ( a.sym == 'i' && b.sym == 'k' ) return element( (-1) * newSgn , 'j' );
}

bool operator !=( element a , element b )
{
    return ( a.sym != b.sym || a.sgn != b.sgn );
}

element getTotal( string s )
{
    element res = element(1 , 'a');
    for ( int i = 0 ; i < s.size(); i++ )
    {
        res = res * element( 1 , s[i] );
        //cout << "Processing " << s[i] << " "<< res.sym << " " << res.sgn << endl;
    }
    return res;
}

int main()
{
    freopen("input.in" , "r" , stdin );
    freopen("output.out", "w" , stdout );

    int T;
    cin >> T;

    for (int _t = 1 ; _t <= T; _t++ )
    {
        int L;
        long long X;
        string s , crap;
        cin >> L >> X;
        getline( cin , crap );
        getline( cin , s );

        element r = getTotal( s );
        if ( r.sym == 'a' && r.sgn == 1 )
        {
            cout << "Case #" << _t << ": " << "NO" << endl;
            continue;
        }

        if ( r.sym == 'a' && r.sgn == -1 && X % 2 == 0)
        {
            cout << "Case #" << _t << ": " << "NO" << endl;
            continue;
        }

        if ( r.sym != 'a' && X % 4 != 2 )
        {
            cout << "Case #" << _t << ": " << "NO" << endl;
            continue;
        }

        string expandedS;
        for (int i = 1; i <= min( X , (long long)superConst ) ; i++)
            expandedS += s;

        element x = element(1 , 'a');
        int i = 0;
        while ( i < expandedS.size() && x != element(1 , 'i') )
        {
            x = x * element(1 , expandedS[i]);
            if (x != element(1 , 'i') ) i++;
        }

        x = element( 1 , 'a');
        int j = expandedS.size() - 1;
        while ( j >= 0 && x != element( 1 , 'k') )
        {
            x = element(1 ,  expandedS[j]) * x;
            if ( x != element( 1, 'k') ) j--;
        }

        if ( i < j )
            cout << "Case #" << _t << ": " << "YES" << endl;
        else
            cout << "Case #" << _t << ": " << "NO" << endl;

    }

    return 0;
}
