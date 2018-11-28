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
#include <iomanip>

using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
     double C,F,X;
     cin >> C>>F>>X;
     double K = 2.0;
     double time = 0.0;
     while( (K+F)*(X-C) >= K*X ){
      time += C/K;
      K+=F;
     }
     time += X/K;
     cout << "Case #" << loop+1 << ": " <<fixed << setprecision(7) <<time<< endl;
   }
   return 0;
}
