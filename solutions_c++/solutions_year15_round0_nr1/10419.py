#include<bits/stdc++.h>
using namespace std;

int main(){
int test , i, j, k, l;
    cin >> test ;
int cases = 0 ;
 while ( test-- ){
    int n ;
    cases++ ;
     cin  >> n ;
     string s ; cin >>s ;
      int  ans = 0 ;
      int sum = 0 ;
      sum += s[0] - '0' ;
      for ( i = 1 ; i <= n ; i++){
       // cout <<" "<<i <<" "<<sum << endl;
          if( sum   < i ){
               ans +=  i - sum ;
               sum  +=  i - sum ;
          }
          sum += s[i] - '0' ;
      }
      cout << "Case #"<<cases <<": "<<ans << endl;
 }
    return 0 ;
}
