#include<iostream>
#include<vector>
using namespace std;

int main(){
  int tc;
  int tmp , a , b ;
  cin >> tc;
  for( int i = 1 ; i <= tc ; ++i ){
     cout << "Case #"<<i<<": ";
     cin >> a ;
     vector<int> V , V2;
     for( int j = 1 ; j <= 4 ; ++j )
         for( int k = 1 ; k <= 4 ; ++k ){
           cin >> tmp;
           if( j == a ) V.push_back(tmp);
         }
     cin >> b;
     for( int j = 1 ; j <= 4 ; ++j )
         for( int k = 1 ; k <= 4 ; ++k ){
           cin >> tmp;
           if( j == b ) V2.push_back(tmp);
         }
     int ans = 0 , res= -1;
     for( int i = 0 ; i < 4 ; ++i )
         for( int j = 0 ; j < 4 ; ++j )
             if( V[i] == V2[j] ) ++ans , res = V[i];
     if( ans == 1 ) cout << res;
     else cout << ( ans ? "Bad magician!" : "Volunteer cheated!");
     cout <<endl;

         
  }
}
