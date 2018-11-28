#include <iostream>
#include <sstream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int C = getInt();
  REP(cc,C) {
    const int n = getInt();
    const int l = getInt();
    string s;
    bool bad = false;
    REP(i,n) {
      cin >> s;
      bool f = true;
      REP(j,l) if(s[j] == '0') {
	f = false;
      }
      if(f) bad = true;
    }
    cin >> s;

    string ans;
    if(bad) {
      ans = "IMPOSSIBLE";
    } else {
      string aa;
      string bb;

      if(l == 1) {
	aa = "0";
	bb = "?";
      } else {

	/*
	  >>> "10" * 25
'10101010101010101010101010101010101010101010101010'
>>> "01" * 25
'01010101010101010101010101010101010101010101010101'
	*/
	stringstream ss; REP(i,l-1) ss << "?";
	aa = ss.str();
	bb = "10101010101010101010101010101010101010101010101010101010?1010101010101010101010101010101010101010101010101010101";
      }

      ans = aa + " " + bb;
    }

    printf("Case #%d: %s\n", cc + 1, ans.c_str());

  }

  return 0;
}



