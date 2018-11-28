#include <bits/stdc++.h>

using namespace std;

set< int > s;

bool extract( long N ){

    while( N > 0 ){
        int r= N%10;
        N/= 10;

        s.insert( r );

        if( s.size()== 10 )
            return true;
    }

    return false;
}

int main(){

    int T;
    long N;

    freopen( "inputLA.in", "r", stdin );
	freopen( "outputLA.txt", "w", stdout );

    cin >> T;

    for( int t= 1; t<= T; ++t ){

        cin >> N;
        int i;

        if( N== 0 ){
            cout << "Case #" << t << ": INSOMNIA" << '\n';
            continue;
        }

        for( i= 1; ; ++i ){
            if( extract( i*N ) )
                    break;
        }

        cout << "Case #" << t << ": " << i*N << '\n';
        s.clear();

    }


}
