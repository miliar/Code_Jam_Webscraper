#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;

char S[20010];
stack<char> st;

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    scanf("%s", S);
    int L = strlen(S);

    int ans = 0;
    for(int i = 0; i < L; i++){
      if(!st.empty() && st.top() == S[i]){
        st.pop(); ans += 10;
      }
      else st.push(S[i]);
    }

    ans += (int)st.size() / 2 * 5;
    printf("Case #%d: %d\n", tt, ans);

    while(!st.empty()) st.pop();
  }
  return 0;
}
