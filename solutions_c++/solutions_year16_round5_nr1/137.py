#include <bits/stdc++.h>
using namespace std;

string S;
int main() {
  int t; cin>>t; for(int zz=1;zz<=t;zz++) {
    cin >> S;
    stack<char> st;
    int ans=0;
    for(char c:S) {
      if(st.empty()||c!=st.top()) st.push(c);
      else st.pop(), ans+=10;
    }
    ans+=5*(st.size()/2);
    printf("Case #%d: %d\n",zz,ans);
  }
}
