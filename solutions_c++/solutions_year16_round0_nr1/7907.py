#include <iostream>

using namespace std;

void solve() {
  int N;
  cin >> N;
  int c[10] = {0,0,0,0,0,0,0,0,0,0};

  for(int i=1;i<=100;i++) {
    int d = i * N;

    while(d) {
      c[d % 10]++;
      d /= 10;
    }

    int s = 0;
    for(int j=0;j<10;j++) {
      if(c[j]) s++;
    }

    if(s == 10) {
      cout << i * N;
      return;
    }
  }
  cout << "INSOMNIA";
}

int main() {
  int T;
  cin >> T;

  for(int i=1;i<=T;i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
