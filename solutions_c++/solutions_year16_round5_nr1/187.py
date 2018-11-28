#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>
#include <stack>

using namespace std;

int main(){
  const int C = getInt();

  REP(cc,C) {
    string s; cin >> s;
    stack<char> st;
    int ret = 0;
    for(const char c : s) {
      if(st.size() && c == st.top()) {
	ret += 10;
	st.pop();
      } else {
	st.push(c);
      }
    }
    ret += st.size() / 2 * 5;
    printf("Case #%d: %d\n", cc + 1, ret);
  }

  return 0;
}
