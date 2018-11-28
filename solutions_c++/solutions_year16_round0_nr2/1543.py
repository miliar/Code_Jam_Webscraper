#include <bits/stdc++.h>
#include <string>
#define FLIP(X) ((X=='+') ? '-' : '+')
using namespace std;

void rotate(string &s, int N) {
  char aux;
  int i;
  for (i=0; 2*i<N; i++) {
    aux = s[i];
    s[i] = FLIP(s[N-i-1]);
    s[N-i-1] = FLIP(aux);
  }
}

int solve(string &s, int N) {
  while(N>0 && s[N-1]=='+') N--;
  if (N==0) return 0;
  int best;
  int bpre=0, bpos=0;
  int pre = 0, pos=0;
  for (int i=1; i<=N; i++) {
    for (pre=0; pre<i; pre++)
      if (s[pre] == '+') break;
    for (pos=0; pos<i; pos++)
      if (s[i-pos-1] == '-') break;
    if (i!=N) pre=0;
    if(pre > bpre || (pre == bpre && pos > bpos)) {
      bpre = pre;
      bpos = pos;
      best = i;
    }
  }

  rotate(s,best);
  return 1 + solve(s,N); //tail recursion is good in c++, right?
}


int main() {
  int T;
  string inp;
  cin >> T;
  for (int t=1; t<=T;t++) {
    cin >> inp;
    cout << "Case #" << t << ": ";
    cout << solve(inp,inp.length()) << endl;
  }
}
