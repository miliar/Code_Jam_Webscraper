#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int input();
int process();
int printResult();

int count;
int length;
int y, z;
long double naomi[1000], ken[1000];

int main ( void ){
    int i;
    int count;

    cin >> count;

    for( i = 0; i < count; i++ ){
        input();
        process();
        cout << "Case #" << i + 1 << ": ";
        printResult();
    }

    return 0;
}

int input(){
    int c;

    cin >> length;
    for( c = 0; c < length; c++ ){
        cin >> naomi[c];    
    }
    for( c = 0; c < length; c++ ){
        cin >> ken[c]; 
    } 

    return 0;
}

int compare( const void *a, const void *b ){
    long double value = ( *( long double * )a - *( long double * )b );
    if( value > 0 ) return 1;
    else if( value < 0 ) return -1;
    else return 0;
}

int sort( long double array[] ){
    std::qsort( array, length, sizeof( long double ), compare ); 
    return 0;
}

int printArray( long double array[] ){
    int c;

    for( c = 0; c < length; c++ ){
        cout << array[c] << ' ';
    }
    cout << endl;
}

int process(){
    y = z = 0;

    sort( naomi );
    sort( ken );

    int cn, ck;
    int lengthKen = length;
    cn = ck = 0;
    while( true ){
        if( cn >= length ) break;
        if( ck >= lengthKen ) break;

        if( naomi[cn] < ken[ck] ) lengthKen--;
        else{
            ck++;
            y++;
        }

        cn++;
    }

    cn = ck = length - 1;
    while( true ){
        while( true ){
            if( ken[ck] > naomi[cn] ) break;
            if( cn < 0 ) break;
            cn--;
        }

        if( cn < 0 ) break;
        if( ck < 0 ) break;

        if( ken[ck] > naomi[cn] ){
            z++;
            ck--;
            cn--;
        }
    }
    z = length - z;

    return 0;
}

int printResult(){
    int i;

    cout << y << ' ' << z << endl;
    
    return 0;
}
