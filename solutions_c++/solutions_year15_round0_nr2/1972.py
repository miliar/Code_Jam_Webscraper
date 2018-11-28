#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

ifstream fin ("in.in");
ofstream fout ("out.txt");

class usp{
public:
    bool operator() ( const int a, const int b ) {
        return a > b;
    }

};
int arr[ 1005 ];

int main () {
    int t; fin >> t; int oldt = t;


    //for ( int i = 0; i < 10; i++ ) cout << dp[ i ] << endl;
    while ( t-- ) {
        int ans = 1000;
        int d; fin >> d;
        for ( int i = 0; i < d; i++ ) {
            fin >> arr[ i ];
        }
        for ( int i = 1; i < 1001; i++ ) {
           int candi = i;
            for ( int j = 0; j < d; j++ ) {
                if ( arr[ j ] <= i ) continue;
                candi += ( arr[ j ] / i ) - 1 + bool( arr[ j ] % i );
            }
            ans = min( ans, candi );
        }
        fout << "Case #" << oldt - t << ": " << ans << endl;

    }
    return 0;
}
