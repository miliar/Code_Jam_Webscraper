#include <iostream>
#include <cstdio>
using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define dforn(i,n) for(int i=(n-1);i>=0;i--)

int palindromos[1024];

bool esPalindromo ( int i )
{
    if ( 0 <= i && i < 10 )
    {
        return true;
    }
    else if ( 10 <= i && i < 100 )
    {
        return ( i%10 == i/10 );
    }
    else if ( 100 <= i && i < 1000 )
    {
        return ( i%10 == i/100 );
    }
    else
    {
        return false;
    }
}

int main ()
{
    freopen("csmall.in","r",stdin);
    freopen("csmall.out","w",stdout);
    int T;
    cin >> T;

    forn(i,1024)
    {
        palindromos[i] = 0;
    }
    forn(i,1024)
    {
        if( esPalindromo(i) )
        {
            palindromos[i] = 1;
        }
    }
    forn(i,32)
    {
        if( palindromos[i] > 0 && palindromos[i*i] > 0 )
        {
            palindromos[i*i] = 2;
        }
    }

    int a, b, res;
    forsn(caso,1,T+1)
    {
        res = 0;
        cin >> a >> b;
        forsn(i,a,b+1)
        {
            if( palindromos[i] == 2 )
            {
                res++;
            }
        }
        cout << "Case #" << caso << ": " << res << endl;
    }
    return 0;
}
