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
    int N;
    int X;
    cin >> N >> X;
    int S[N];
    for( int i = 0 ; i < N ; i++ ) cin >> S[i];
    int n_small=0;
    sort(S,S+N);
    int cnt = 0;
    for( int i = N-1; i>= 0 ; i-- ){
      if( i < n_small ) break;
      if( S[i]+S[n_small] <= X ){
        n_small++;
      }
      cnt++;
    }
    cout << "Case #" << loop+1 << ": " <<cnt<< endl;
  }
  return 0;
}
