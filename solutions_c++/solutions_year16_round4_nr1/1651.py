#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

ifstream fi;

bool p2(string &ret, int n, int p, int r, int s) {
  string str;
  for (int i=0; i<n; i++) {
    str = ret;
    ret = "";
    for (int j=0; j<str.size(); j++) {
      if (str[j] == 'P') {
        ret += "PR";
      }
      else if (str[j] == 'R') {
        if (n-1 == i)
          ret += "RS";
        else
          ret += "SR";
      }
      else {
        if (n-2 <= i)
          ret += "PS";
        else
          ret += "SP";
      }
    }
  }
  for (int j=0; j<ret.size(); j++) {
    if (ret[j] == 'P') p--;
    else if (ret[j] == 'R') r--;
    else s--;
  }
  return (p==0 && r==0 && s==0);
}

bool p1(string str,string &ret, int n, int p, int r, int s) { ret=str; return p2(ret,n,p,r,s); }

void process() {
  int n,r,p,s;
  fi >> n >> r >> p >> s;
  string ret;
  if (p1("P",ret,n,p,r,s))
    cout << ret;
  else if (p1("R",ret,n,p,r,s))
    cout << ret;
  else if (p1("S",ret,n,p,r,s))
    cout << ret;
  else
    cout << "IMPOSSIBLE";
}

int main(int argc, char **argv) {
  if (argc > 1)
    fi.open(argv[1]);
  else
    fi.open("input.txt");
  int c;
  fi >> c;
  for (int i=0; i<c; i++) {
    cout << "Case #" << (i+1) << ": ";
    process();
    cout << endl;
  }

  return 0;
}
