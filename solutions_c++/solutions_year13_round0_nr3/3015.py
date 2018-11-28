#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
const double eps = 1e-6;

int main() {
    int T, n, m ;
    cin>>T;
    for( int tc = 1; tc <= T; ++tc ) {
         cin>>n>>m;
         int ret = 0;
         for( int i = n; i <= m; ++i ) {
              int a = (int)( sqrt(i*1.0) + eps );
              bool ok = true;
              if( a*a != i ) continue;
              stringstream s;
              s<<i;
              string str;
              s>>str;
              //cout<<"str="<<str<<endl;
              for( int j = 0 ; j <= str.size()/2; ++j ) if( str[j] != str[str.length()-j-1] ) ok = false;
              s.flush(); s.clear();
              s<<a;
              s>>str;
              //cout<<str<<endl;
              for( int j = 0 ; j <= str.size()/2; ++j ) if( str[j] != str[str.length()-j-1] ) ok = false;
              //if( ok ) cout<<i<<endl;
              ret += ok; 
         }
         cout<<"Case #"<<tc<<": "<<ret<<endl;
    }
    return 0;
}
