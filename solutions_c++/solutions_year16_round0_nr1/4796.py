#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <math.h>
#include <iostream>

using namespace std;
typedef long long ll;

ll last_num(int n) {
  if (n == 0) {
    return -1;
  }
  ll tr = 0;
  int a [10] = {0};
  while (a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9] == 0) {
    ll cp = tr;
    while (cp > 0) {
      a[cp%10]++;
      cp /= 10;
    }
    tr += n;
  }
  return tr-n;
}

int main() {
  ifstream fin;
  fin.open ("anne.in");
  ofstream fout;
  fout.open ("anne.out");
  
  int t; fin >> t;
  
  for (int i=0; i<t; i++) {
    int n; fin >> n;
    ll ans = last_num(n);
    fout << "Case #" << i+1 << ": ";
    if (ans == -1) {
      fout << "INSOMNIA" << endl;
    } else {
      fout << ans << endl;
    }
  }
  
  
  


}