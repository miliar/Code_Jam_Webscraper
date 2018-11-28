#include <iostream>
#include <stdio.h>

using namespace std;


int solve(){

    int fr, fcards[4] = { 0 }, sr, scards[4] = { 0 }, card, res = 0, bla[4];

    cin >> fr;
    for( int i = 0; i < 4; i++ ){
        if( i != (fr-1) ) cin >> bla[0] >> bla[1] >> bla[2] >> bla[3];
        else cin >> fcards[0] >> fcards[1] >> fcards[2] >> fcards[3];
     }

    cin >> sr;
    for( int i = 0; i < 4; i++ ){
        if( i != (sr-1) ) cin >> bla[0] >> bla[1] >> bla[2] >> bla[3];
        else cin >> scards[0] >> scards[1] >> scards[2] >> scards[3];
    }

    for( int i = 0; i < 4; i++ ){

        for( int j = 0; j < 4; j++ ) if( fcards[i] == scards[j] ){ card = scards[j]; res++; }

    }

    if( res == 0 ) return 0;
    if( res == 1 ) return card;
    if( res > 1  ) return -1;

}


int main()
{
    int p, num = 1;
    cin >> p;

    while( p-- ){

        char *r = "";
        int n=0, v;
        v=solve();

        if( v == 0 ) r = "Volunteer cheated!";
        else if( v == -1 ) r = "Bad magician!";
        else n = v;

        cout << "Case #" << num++ << ": " << r;
        if( n != 0 ) cout << n;
        cout << "\n";

    }

    return 0;

}

