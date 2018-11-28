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

int bitCount( int mask ){
   int cnt=0;
   while( mask != 0 ){
      cnt++;
      mask &= mask-1;
   }
   return cnt;
}

int main(){
  int n_case;
  cin >> n_case;
  for( int loop = 0 ; loop < n_case ; loop++ ){
   int N, K;
   cin >> N >> K;
   double p[N];
   for( int i = 0 ; i < N; i++ ){
      cin >> p[i];
   }
   double ans =0;
   for( int mask =0; mask < (1<<N); mask++){
      if(bitCount(mask)==K){
         //cout << "mask:" << mask << endl;
         double tmpAns=0;
         for( int mask2=0; mask2 <(1<<N); mask2++){
            //cout <<"mask2:" << mask2 << endl;
            if(bitCount(mask2)==K/2 && (mask&mask2)==mask2){
               double curAns=1;
               for( int i=0; i < N; i++ ){
                  if( mask&(1<<i) ){
                     if( mask2&(1<<i) ){
                        curAns*=p[i];
                     }
                     else{
                        curAns*=1.0-p[i];
                     }
                  }
               }
               tmpAns+=curAns;
            }
         }
         ans=max(ans,tmpAns);
      }
   }
   printf("Case #%d: %.10f\n",loop+1, ans);
  }
return 0;
  
}
