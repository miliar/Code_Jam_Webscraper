# include <iostream>
# include <string>
using namespace std ;

int main ()
{

    int t , s , total , add ;

    cin >> t ;

    for( int i = 1 ; i <= t; i++)
    {
        cin >> s ;

        int u = s + 1 ;

        int a[u] ;

        string st ;

        cin >> st;

        int p ;
        add = 0 ;
        total = 0 ;

        for( int j = 0 ; j < u ; j++ )
        {
            a[j] = st[j] - '0' ;

            if( j > total )
            {
                p = j - total ;
                add = add + p ;
                total = total + p ;
            }

            total = total + a[j] ;
        }

        cout <<"Case #"<<i<<": "<<add << endl ;

    }
	return 0;

}
