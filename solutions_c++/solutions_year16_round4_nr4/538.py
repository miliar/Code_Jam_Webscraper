#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

inline int popcount(int bmap) {
  int resp=0;
  while (bmap>0) {
    resp += (bmap&1);
    bmap>>=1;
  }
  return resp;
}



bool isValid(const vector<string>& able, int usedmap=0, int workmap=0) {
  if (workmap+1 == (1<<(able.size())))
    return true;
  for (int w=0; w<able.size(); ++w) if(!(workmap & (1<<w))) {
    bool oneable=false;
    for (int a=0; a<able.size(); ++a) if(able[w][a]=='1' && !(usedmap & (1<<a))) {
      if (!isValid(able, usedmap | (1<<a), workmap | (1<<w)))
        return false;
      else
        oneable = true;
    }
    if (!oneable)
      return false;
  }
  return true;
}

int main() {
  int t;
  cin >> t;
  for (int ta=1; ta<=t; ++ta) {
    cout << "Case #" << ta << ": ";
    int n;
    cin >> n;
    vector<string> able(n);
    for (int i=0;i<n;++i)
      cin >> able[i];
    
    int best = n*n;
    for (int bmap=0; bmap<(1<<(n*n)); ++bmap) if(popcount(bmap) < best){
      vector<string> newable = able;
      bool valid=true;
      for (int b=0; b<(n*n) && valid;++b) if(bmap & (1<<b)) {
        int r=b/n, c=b%n;
        if (able[r][c] == '1')
          valid = false;
        else
          newable[r][c] = '1';
      }
      if (valid && isValid(newable))
        best = popcount(bmap);
    }
    cout << best << endl;
  }
}