#include <iostream>
using namespace std;
int d[17];
int main( void )
{
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    for( int i=1; i<=16; i++ ) d[i]=0;
    for( int i=0; i<2; i++ ){
      int a,b;
      cin >> a;
      for( int j=1; j<=4; j++ ){
        for( int k=1; k<=4; k++ ){
          cin >> b;
          if( j == a ) d[b]++;
        }
      }
    }
    int num=0;
    int ans=0;
    for( int i=1; i<=16; i++ ){
      if( d[i]==2 ){
        ans = i;
        num++;
      }
    }
    if( num == 1 ){
      cout << "Case #" << testcase << ": " << ans << endl;
    } else if( num > 1 ){
      cout << "Case #" << testcase << ": " << "Bad magician!" << endl;
    } else {
      cout << "Case #" << testcase << ": " << "Volunteer cheated!" << endl;
    }
  }
  return 0;
}
