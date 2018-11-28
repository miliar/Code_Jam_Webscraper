#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <vector>
#include <string>
#include <set>
#include <stdlib.h>

using namespace std;
typedef long long int ll;

int T;
int N;
int J;

const int STOCK_PRIME = 1000000;

//#define ___IN___ cin
//#define ___OUT___ cout
ifstream fin;
ofstream fout;
#define ___IN___ fin
#define ___OUT___ fout

set<ll> sStockPrime;

const int MAX_N = 32;

ll baseCalc[11][MAX_N];

ll pow( ll base, ll digit ) {
    ll ret = 1;
    for( int d=0; d<digit; d++ ) {
        ret *= base;
    }
    return ret;
}


void calcBase() {
    
    memset( baseCalc, 0x00, sizeof(baseCalc) );
    
    for( int b=2; b<=10; b++ ) {
        for( int d=0; d<MAX_N; d++ ) {
            baseCalc[b][d] = pow( b, d );
        }
    }
}


void sieve(ll ub) {
    bitset<STOCK_PRIME> bs; // UINT_MAXだと足りないかもしれないが・・・
    bs.set();   // initialize set the all bit
    bs[0]=bs[1]=0;
    
    for(ll i=2; i<=ub+1; i++) {
        if( bs[i] ) {
            for( ll j=i*i; j <= ub+1; j+=i ) {
                bs[j]=0;
            }
            sStockPrime.insert(i);
        }
    }
}

bool IsPrime(ll val) {
    if( val <= STOCK_PRIME ) {
        return (sStockPrime.find(val)!=sStockPrime.end());
    }
    
    // out of stock
    for( ll i=2; i*i <= val; i++ ) {
        if( val % i == 0 ) return false;
    }
    
    return true;
}

ll getDivisor(ll val) {
    // 2 is OK?
    //for( ll i=2; i*i < val; i++ ) {
    for( ll i=3; i*i < val; i++ ) {
        if( val % i == 0 ) return i;
    }
    // 2はなんとなく最後の手段に・・・！
    return ( val % 2 ) == 0 ? 2 : -1;   // !!
}


class JamCoin {
    bitset<32> bs;
    
    ll base[11];
    
public:
    JamCoin( const bitset<32>& bs_ ) : bs( bs_ )
    {
        memset( base, 0x00, sizeof(base) );
        
        for( int i=0; i<N; i++ ) {
            for( int b=2; b<=10; b++ ) {
                if( bs[i] == 1 ) {
                    base[b] += baseCalc[b][i];
                }
            }
        }
    }
    
    bool validate() {
        for( int b=2; b<=10; b++ ) {
            if( IsPrime(base[b]) ) return false;
        }
        return true;
    }
    void output() {
        
        string str = bs.to_string();
        str=str.substr( str.size()-N );
        
        ___OUT___ << str;
        
        // outputNontrivialDivisors
        for( int b=2; b<=10; b++ ) {
            ___OUT___ << " " << getDivisor(base[b]); //<< "(" << base[b] << ")";
        }
        ___OUT___ << endl;
    }
    
};



void CreateJamCoins() {
    
    int number = 1;
    ___OUT___ << "Case #" << number << ":" << endl;
    
    bitset<32> bs;
    
    // This while is not need becase below note.
    // It is guaranteed that at least J distinct jamcoins of length N exist.
    //        while( 0 < J ) {
    
    for( int p=0; p<(1<<(N-2)); p++ ) {
        // {0},{1},...{0,1,...,n-1}
        
        bs.reset();
        // The first digit is 1 and the last digit is 1.
        bs[0] = 1;
        bs[N-1] = 1;
        
        bs |= p<<1;
        
        //        ___OUT___ << bs << endl;
        
        JamCoin jamCoin(bs);
        
        if( jamCoin.validate() ) {
            jamCoin.output();
            if( --J <= 0 ) break;
        }
    }
    //        }
}

void solve() {
    
    sieve( STOCK_PRIME );
    calcBase();
    
    //    ___OUT___ << sStockPrime.size() << endl;
    
    CreateJamCoins();
}




int main(int argc, char** argv) {
    if( argc != 3 ) {
        cout << "usage:exe in out" << endl;
    }
    string infile=argv[1];
    fin.open(infile, std::ios::in);
    
    string outfile=argv[2];
    fout.open(outfile, std::ios::out);
    
    // The first line of the input gives the number of test cases, T.
    //cin >> T;
    ___IN___ >> T;
    // T test cases follow.
    while( T-- ) {
        ___IN___ >> N >> J;
        solve();
    }
    fin.close();
    fout.close();
    cout << "end" << endl;
    return 0;
}


