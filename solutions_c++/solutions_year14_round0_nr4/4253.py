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

int calcScore(vector<double> A, vector<double> B){
  int N =  A.size();
  int seriousScore = N;
  for( int i = 0 ; i < N ; i++ ){
    if( lower_bound( B.begin(), B.end(), A[i] ) != B.end() ){
      seriousScore--;
      B.erase(lower_bound(B.begin(),B.end(),A[i])); 
    }
    else{
      B.erase(B.begin()); 
    }
  }
  return seriousScore;
}

int main(){
  int n_case;
  cin >> n_case;
  for( int loop = 0 ; loop < n_case ; loop++ ){
    int N;
    cin >> N;
    vector<double> A;
    vector<double> B;
    for( int ai = 0 ; ai < N ; ai++ ){
      double a;
      cin >> a;
      A.push_back(a);
    }
    for( int bi = 0 ; bi < N ; bi++ ){
      double b;
      cin >> b;
      B.push_back(b);
    }
    sort( A.begin(), A.end() );
    sort( B.begin(), B.end() );
    int cheatScore = N-calcScore(B,A);
    int seriousScore = calcScore(A,B);
    cout << "Case #" << loop+1 << ": " <<cheatScore << " " << seriousScore << endl;
  }
  return 0;
}
