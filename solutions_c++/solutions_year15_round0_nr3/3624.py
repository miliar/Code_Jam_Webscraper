#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <sstream>
#include <cstdlib>

#define ULL unsigned long long int

using namespace std;

typedef struct Cake{
    unsigned long long int repts;
    unsigned long long int l;
    std::string seq;
    unsigned long long int curr_idx = 0;
    char operator[]( unsigned long long int idx ){
        return (idx < l*repts) ? seq[idx%l] : 0;
    }
    ULL len(){return ( l * repts );}
} Cake;

Cake readCase( istream& fin ){
    Cake c;
    fin >> c.l >> c.repts >> c.seq;
    //std::cout << "L: " << c.l << " X: " << c.repts << " str: " << c.seq << std::endl;
    return c;
}

char multiply( char a, char b){
    //l is 1, caps for negated

    if(a==b) return (a=='l' || a=='L') ? 'l' : 'L';

    bool neg = false;
    if( a < 100 ){
        a += 32;
        neg = !neg;
    }
    if( b < 100 ){
        b += 32;
        neg = !neg;
    }
    char r;

    switch(a){
        case 'l': r = b; break;
        case 'i': 
            if(b=='l') r = a;
            if(b=='i') r = 'L';
            if(b=='j') r = 'k';
            if(b=='k') r = 'J';
            break;
        case 'j':
            if(b=='l') r = a;
            if(b=='i') r = 'K';
            if(b=='j') r = 'L';
            if(b=='k') r = 'i';
            break;
        case 'k':
            if(b=='l') r = a;
            if(b=='i') r = 'j';
            if(b=='j') r = 'I';
            if(b=='k') r = 'L';
            break;
    }
    if( r < 100 ){
        r += 32;
        neg = !neg;
    }
    
    return neg ? r-32 : r ;
}

ULL findEnd( char desired, ULL start, Cake &c ){
    char d = c[start];
    int idx = start;
    while(d!=desired){
        idx++;
        char b = c[idx];
        if(b)
            d = multiply( d, b);
        else
            return -1;
    }
    return idx;
}

void doCase( Cake c ){
    ULL iStart = 0;
    ULL iEnd;
    ULL jEnd;
    ULL kEnd;

    iEnd = findEnd( 'i', iStart, c );
    //cout << "i" << iEnd;
    if( iEnd == -1 ){
        cout << "NO";
        return;
    }

    jEnd = findEnd( 'j', iEnd+1, c );
    //std::cout << 'j' << jEnd;
    if( jEnd == -1 ){
        cout << "NO";
        return;
    }

    kEnd = findEnd( 'k', jEnd+1, c);
    //cout << 'k' << kEnd;
    if( kEnd == -1 ){
        cout << "NO";
        return;
    } else if ( kEnd == c.len()-1 ){
        cout << "YES";
        return;
    }
    ULL end = findEnd( 'l', kEnd+1, c);
    while(end != c.len()-1){
        end = findEnd( 'l', end+1, c);
        if( end == -1 ){
            cout << "NO";
            return;
        }
    }
    //cout << '1' << end;
    cout << "YES";
    return;
}

void testMul(){
    char zz[9] = "lijkLIJK";
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            std::cout << multiply( zz[i], zz[j] ) << " ";
        }
        std::cout << endl;
    }
}

int main(int argc, const char *argv[])
{
    //testMul();
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    char c[10000];
    fin.getline(c,10000);
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";
        auto c = readCase( fin );
        doCase( c );
        std::cout << std::endl;

    }

    return 0;
}
