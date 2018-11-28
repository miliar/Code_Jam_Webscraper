#ifndef QUALIFICATION_ROUND_2015A_H
#define QUALIFICATION_ROUND_2015A_H

#include "utils.h"

int main(int argc, char *argv[]) {
  if(argc >= 2) {
    freopen (argv[1],"r",stdin);
  }
  int T;
  cin >>  T;
  for(int t=0;t<T;++t) {
    int shy;
    cin >> shy;
    string s;
    cin >> s;
    vector<int> noms;
    noms.resize(s.size());
    for(int i=0;i<s.size();++i) {
      noms[i] = s[i] - '0';
    }
    int nos = 0;
    int extra = 0;
    for(int i=0;i<s.size();++i) {
      if(nos < i) {
        extra += i - nos;
        nos += i - nos;
      }
      nos += noms[i];
    }
    cout << "Case #" << t + 1 << ": " << extra << endl;
  }


  return 0;
}


#endif // QUALIFICATION_ROUND_2015A_H
