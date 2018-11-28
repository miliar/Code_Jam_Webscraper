#include <bits/stdc++.h>

using namespace std;

void solveCase()
{
  char S[1111];
  deque<char> dq;
  scanf("%s\n", S);
  for (int i=0; i<strlen(S); i++) {
    if (S[i] >= dq.front()) {
      dq.push_front(S[i]);
    } else {
      dq.push_back(S[i]);
    }
  }
  for (int i=0; i<strlen(S); i++) {
    cout << dq[i];
  }
  cout << endl;
}

int main ()
{
  int T;
  cin >> T;
  for (int i=1; i<=T; i++) {
    printf("Case #%d: ", i);
    solveCase();
  }
  return 0;
}
