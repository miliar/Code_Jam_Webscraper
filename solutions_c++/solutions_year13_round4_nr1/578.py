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
   int mod = 1000002013;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      int N, M;
      cin >> N >> M;
      vector< pair<int,int> > be;
      vector< pair<int,int> > en;
      long long totpay=0;
      for( int i = 0 ; i < M; i++ ){
        int o, e, p;
        cin >> o >> e>>p;
        be.push_back( make_pair(o,-1*p) );
        be.push_back( make_pair(e,p) );
        int dist = e-o;
        totpay +=  ((2*N-dist+1)*dist/2)*p;
      }
      sort( be.begin(), be.end() );
      long long totpay2 = 0;
      int size = be.size();
      for( int i = 0 ; i < size; i++ ){
        pair<int,int> bep = be[i];
        int nextpos = bep.first;
        int nextnum = bep.second;
        if( nextnum > 0 ) continue;
        int curnum = nextnum;
        for( int j = i+1 ; j < size; j++ ){
          pair<int,int> tmp = be[j];
          int tmppos = tmp.first;
          int tmpnum = tmp.second;
          //cout << curnum << endl;
          curnum += tmpnum;
          if( curnum >= nextnum ){
            int oriru = min( curnum-nextnum,-1*nextnum );
            //cout << curnum+1 << "vs" << -1*nextnum<<endl;
            int dist = tmppos-nextpos;
            totpay2 += ((2*N-dist+1)*dist/2)*oriru;
            //cout << nextpos << "-" << tmppos << ":" << oriru << endl;
            nextnum += oriru;
          }
          if( nextnum == 0 ) break;
        }
      }
      //cout << totpay <<"vs" << totpay2 << endl;
     cout << "Case #" << loop+1 << ": " ;
     cout << totpay-totpay2<<endl;
   }
   return 0;
}
