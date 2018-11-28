// Google Code Jam 2016
// Phase 1
// Revenge of the Pancakes

#include <bits/stdc++.h>

using namespace std;

string s;

int check() {
  for(int j = s.length() - 1; j >= 0; j--) {
    if (s[j] == '-') return j;
  }
  return -1;
}

void turn(int v) {
  for (int i = 0; i <= v; i++) {
    if (s[i] == '+') s[i] = '-';
    else s[i] = '+';
  }
}

int main() {
  int n;
  cin >> n;

  for (int i = 1; i <= n; i++) {
    cin >> s;
    int r = 0;

    while(1) {
      int v = check();
      if (v != -1) {
        turn(v);
        r++;
      } 
      else break;
    }

    cout << "Case #" << i << ": " << r << endl;
    
  }
  return 0;
}
