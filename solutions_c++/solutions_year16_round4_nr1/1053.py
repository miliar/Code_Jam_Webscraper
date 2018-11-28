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

int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      int N,R,P,S;
      cin >> N >> R >> P >> S;
      int M=max(R,max(P,S));
      int m=min(R,min(P,S));
      if ( M>m+1 ){
         cout << "Case #" << loop+1 << ": "<<"IMPOSSIBLE"<<endl;
      }
      else{
         string str[3]={"R","S","P"};
         for( int i = 0 ; i <N; i++ ){
            string nxt[3]={"","",""};
            for( int j = 0 ; j < 3; j++ ){
               int remain = (N-1-i)%6;
               for( int k = 0 ; k < (int)str[j].size(); k++ ){
                  if( str[j][k]=='R' ){
                     if( remain == 0 || remain == 4 || remain == 5 )nxt[j]+="RS";
                     else nxt[j]+="SR";
                  }
                  else if( str[j][k]=='S' ){
                     if( remain == 2 || remain == 3 || remain == 4 ) nxt[j]+="SP";
                     else nxt[j]+="PS";
                  }
                  else{
                     if( remain == 0 || remain == 1 || remain == 2 ) nxt[j]+="PR";
                     else nxt[j]+="RP";
                  }
               }
               str[j]=nxt[j];
            }
         }
         for( int i = 0 ; i < 3; i++ ){
            int r=0,p=0,s=0;
            for( int k = 0 ;k <(int)str[i].size();k++){
               if( str[i][k]== 'R') r++;
               if( str[i][k]== 'S') s++;
               if( str[i][k]== 'P') p++;
            }
            if( r==R && p==P && s==S){
               cout << "Case #" << loop+1 << ": " << str[i]<<endl;
               break;
            }
         }
      }
   }
   return 0;
}
