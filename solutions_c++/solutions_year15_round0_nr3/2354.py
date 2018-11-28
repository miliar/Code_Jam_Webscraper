#include <bits/stdc++.h>
using namespace std;

int M0[256][256];
int M1[256][256];

void setup() {
  M0[1][1] = 1;
  M1[1][1] = 1;  
  M0[1][int('i'-'a')] = 1;
  M1[1][int('i'-'a')] = int('i'-'a');  
  M0[1][int('j'-'a')] = 1;
  M1[1][int('j'-'a')] = int('j'-'a');  
  M0[1][int('k'-'a')] = 1;
  M1[1][int('k'-'a')] = int('k'-'a');  

  M0[int('i'-'a')][1] = 1;
  M1[int('i'-'a')][1] = int('i'-'a');
  M0[int('i'-'a')][int('i'-'a')] = -1;
  M1[int('i'-'a')][int('i'-'a')] = 1;
  M0[int('i'-'a')][int('j'-'a')] = 1;
  M1[int('i'-'a')][int('j'-'a')] = int('k'-'a');
  M0[int('i'-'a')][int('k'-'a')] = -1;
  M1[int('i'-'a')][int('k'-'a')] = int('j'-'a');

  M0[int('j'-'a')][1] = 1;
  M1[int('j'-'a')][1] = int('j'-'a');
  M0[int('j'-'a')][int('i'-'a')] = -1;
  M1[int('j'-'a')][int('i'-'a')] = int('k'-'a');
  M0[int('j'-'a')][int('j'-'a')] = -1;
  M1[int('j'-'a')][int('j'-'a')] = 1;
  M0[int('j'-'a')][int('k'-'a')] = 1;
  M1[int('j'-'a')][int('k'-'a')] = int('i'-'a');

  M0[int('k'-'a')][1] = 1;
  M1[int('k'-'a')][1] = int('k'-'a');
  M0[int('k'-'a')][int('i'-'a')] = 1;
  M1[int('k'-'a')][int('i'-'a')] = int('j'-'a');
  M0[int('k'-'a')][int('j'-'a')] = -1;
  M1[int('k'-'a')][int('j'-'a')] = int('i'-'a');
  M0[int('k'-'a')][int('k'-'a')] = -1;
  M1[int('k'-'a')][int('k'-'a')] = 1;

}

void solve(int t) {
  int L, X;
  cin >> L >> X;
  string s;
  cin >> s;
  string S;
  for (int i=0; i<X; i++)
    S += s;

  vector<bool> Memo(S.length(), false);
  int right = 1, signright = 1;
  for (int i = S.length()-1; i >= 0; i--) {
      signright *= M0[int(S[i]-'a')][right];  
      right = M1[int(S[i]-'a')][right];
      if (right == int('k'-'a') &&
          signright == 1) Memo[i] = true;
  }

  bool res = false;
  
  int signleft = 1;
  int left = 1;
  for (int i = 0;
        !res && i < S.length()-2; i++) {
    signleft *= M0[left][int(S[i]-'a')];  
    left = M1[left][int(S[i]-'a')];
    if (!(left == int('i'-'a') &&
          signleft == 1)) continue;
    int signmid = 1;
    int mid = 1;
    for (int j = i+1;
          !res && j < S.length()-1; j++) {
      signmid *= M0[mid][int(S[j]-'a')];  
      mid = M1[mid][int(S[j]-'a')];
      if ((mid == int('j'-'a') &&
           signmid == 1 && Memo[j+1])) res = true;
    }
  }

  if (res)
    printf("Case #%d: YES\n", t);
  else
    printf("Case #%d: NO\n", t);
}


int main(void) {
  setup();
	int T; cin >> T;
  for (int t=1; t<=T; t++) solve(t);  
}
