#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <gmpxx.h>

using namespace std;


void solve(void);
void _solve(int k, int c, int s);

int main(int argc, char* argv[]){
  solve();
  return 0;
}

#define LINESIZE 2000
ofstream of;

void solve(){

  ifstream fl;
  fl.open("f1.in");
  of.open("f1.out");

  int t, k, c, s, i;
  fl >> t;
  for (i = 0; i < t; i++){
    fl >> k;
    fl >> c;
    fl >> s;
    of << "Case #" << (i+1) << ":";
    _solve(k,c,s);
  }

  fl.close();
  of.close();
}


void _solve(int k, int c, int s){

  int p = k/(c+1);
  if ((k % (c+1)) == 0)
    p = p + 1;

  if (s < p){
    of << "IMPOSSIBLE" << endl;
    return;
  }

  if (k == s){
    int i;
    for (i = 0; i < k; i++)
      of << ' ' << (i + 1);
    of << endl;
    return;
  }
  
  if (c >= k)
    c = (k - 1);

  // too lazy for direct math result
  int off, start = 0, ct;
  mpz_class index, b;
  while (start < k){
    b = 0;
    off = start;
    ct = c;
    while (ct > 0){
      ct = ct - 1;
      b = k * (b + off);
      off = off + 1;
    }
    index = b + off;
    of << ' ' << (index + 1);
    start = off + 1;
  }
  of << endl;
}
