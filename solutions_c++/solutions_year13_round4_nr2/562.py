#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;
long long  bitcount( long long N ){
  long long  count = 0;
  while( N != 0) {
    count++;
    N &= (N-1);
  }
  return count;
}
int  main(){
   long long  n_case;
   cin >> n_case;
   for( long long  loop = 0 ; loop < n_case ; loop++ ){
     long long  N,  P;
     cin >> N >> P;
     long long  n_round=0;
     long long tmpN=(1LL<<N);
     long long tmpP=P;

     if( tmpN == P ){
         cout << "Case #" << loop+1 << ": " ;
         cout << tmpN-1 << " " << tmpN-1 << endl;
         continue;
     }
     
     while( tmpP > tmpN/2 ){
        n_round++;
        tmpN/=2;
        tmpP-=tmpN;
     }
//     cout << "must win at" << n_round<<"-th round "<< endl;
     long long y =0;
     for( long long  i = 0 ; i < n_round ; i++ ){
      y = 2*(y+1);
     }
      
     long long tmp = (1LL<<N)-1;
     long long  curP = P-1;
     while( curP < tmp ){
      tmp /= 2;
     }
     long long  n = bitcount( tmp );
//     cout << "must win " << N-n << "times"<<endl;
     long long z = (1LL<<N)-1;
     for( long long  i = 0 ; i < N-n ; i++ ){
      z -= (1LL<<i);
     }
     
     cout << "Case #" << loop+1 << ": " ;
         cout << y << " " << z << endl;
   }
   return 0;
}
