#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <math.h>
#include <iostream>

using namespace std;
typedef long long ll;

int min_flips(string s) {
  int i = 0;
  char cur = s[0];
  int count = 0;
  
  while (i < s.size()) {
    while (i < s.size() && s[i] == cur) {
      i++;
    }
    count++;
    if (i < s.size()) {
      cur = s[i];
    }
  }
  
  if (cur == '-') return count;
  return count - 1;
}

int main() {
  ifstream fin;
  fin.open ("anne.in");
  ofstream fout;
  fout.open ("anne.out");
  
  int t; fin >> t;
  for (int i=0; i<t; i++) {
    string s; fin >> s;
    int ans = min_flips(s);
    fout << "Case #" << i+1 << ": " << ans << endl;
  }
}