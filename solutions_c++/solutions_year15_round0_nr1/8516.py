#include <iostream>
#include <cstdio>
using namespace std;

const int MAX = 1005;
int a[MAX];
void toNum( string v, int m_ ) {
   for( int i = 0; i <= m_; ++i ){
         a[i] = v.at(i) - '0';
   }
}
void solve()
{
   int T;
   cin >> T;
   int t = 0;
   while( T-- ) {
      int max_;
      string value;
      cin >> max_;
      cin >> value;
      toNum( value, max_ );
      int totalNum = a[0];
      int need = 0;
      for( int i = 1; i <= max_; ++i ) {
         if( totalNum < i ) {
            int tmp = i - totalNum;
            need += tmp;
            totalNum += tmp;
         }
         totalNum += a[i];
      }
      cout << "Case #" << ++t << ": " << need << endl;
   }
}
int main()
{
   freopen( "in", "r", stdin );
   freopen( "out", "w", stdout );
   solve();
   return 0;
}
