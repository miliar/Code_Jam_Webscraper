#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define PI 3.1415926535
#define EPS 1e-9

int main(){
  int T;
  long long r, t;
  cin >> T;
  for(int cs = 0 ; cs < T ; cs++){
    cin >> r >> t;
    //r += 1.0;
    
    int circle = 0;
    
    long long  C = 1+r*2;
    
    while(t >= 0){
      //cout << t << endl;
      //cout << C << endl;
      t -= C;
      if(t < 0) break;
      circle++;
      C += 4;
    }
    /*    
    r += 1.0;
    while(t >= 0.0){
      //cout << t << endl;
      //double b = (double)(r*r*PI);
      //double w = (double)((r-1)*(r-1)*PI);
      //double tt = (b-w) / PI;
      //int p = (int)tt;
      //cout << "tt = " << tt << endl;
      t -= ((r*r*PI) - ((r-1)*(r-1)*PI)) / PI;
      cout << ((r*r*PI) - ((r-1)*(r-1)*PI)) / PI << endl;
      //t -= p;
      if(t < 0.0) break;
      circle++;
      r+=2.0;
    }
    */
    cout << "Case #" << cs+1 << ": " << circle << endl;
  } 
  return 0;
}
