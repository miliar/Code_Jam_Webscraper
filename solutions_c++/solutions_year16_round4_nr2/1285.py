#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <fstream>
#include <map>
#include <set>

using namespace std;

typedef long long ll;

int main() {
  ifstream myfile;
  myfile.open ("awesome.in");
  ofstream a_file ( "example.out");
  
  int t; myfile >> t;
  for(int i = 0; i < t; i++) {
    int n, k; myfile >> n >> k;
    double p[n];
    double max = 0;
    for(int j = 0; j < n; j++) myfile >> p[j];
    vector<bool> dk(n);
    fill(dk.begin() + n - k, dk.end(), true);
    vector<bool> mv(n);
    do {
    		vector<double> sel;
    		for(int j = 0; j < n; j++) {
          if(dk[j]) sel.push_back(p[j]);
          
        }
      double rep = 0;
      vector<bool> gah(k);
      fill(gah.begin() + k/2, gah.end(), true);
      do{
        double mep = 1;
        for(int j = 0; j < k; j++) {
          if(gah[j]) mep *= sel[j];
          else mep *= 1 - sel[j];
        }
        rep += mep;
      } while(next_permutation(gah.begin(), gah.end()));
      if(max < rep) {
        max = rep;
        mv = dk;
      }
    } while (next_permutation(dk.begin(), dk.end()));
    a_file << "Case #" << i+1 << ": " << max << endl;
  }
  return 0;
}
