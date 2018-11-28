// Google Code Jam 2016
// Phase 1
// Counting Sheep

#include <bits/stdc++.h>

using namespace std;

long long v;
int a[10];

int check(long long val){
  string s = to_string(val);
//  cout << val << endl;
  for(int i = 0; i < s.length(); i++) {
//    cout << a[(int)s[i]] << endl;
    a[((int)s[i]) - '0'] = 1;
  }
  for (int j = 0; j < 10; j++) {
    if(a[j] == 0) {
      return 0;
    }
  }
  return 1;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    bool fim = false;
    memset(a, 0, sizeof a);

    cin >> v;
    int j;
    for (j = 1; j < 200; j++){
      if (check(v * j)) {
        fim = true;
        break;
      }
    }

    cout << "Case #" << i << ": ";
    if(fim) cout << v * j << endl; 
    else cout << "INSOMNIA\n";
  }
  return 0;
}

