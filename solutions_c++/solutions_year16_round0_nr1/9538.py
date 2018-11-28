#include <iostream>
#include <string>

using namespace std;

void updateSeen(long x, bool *seen) {
  while (x > 0) {
    seen[x%10]=true;
    x/=10;
  }
}

long getSteps(long x) {
  bool seen[10];
  memset(seen, false, sizeof(seen));
  if (x == 0) return -1;
  for (long step = 1; step <= 100000; step++) {
    updateSeen(x * step, seen);
    int cnt = 0;
    for (int i = 0; i < 10; i++) {
      if (seen[i])cnt++;
    }
    if (cnt == 10) return x * step;
  }
  return -1;
}

int main() {
  //int N = 1000000;
  int N;
  int nt = 0;
  long start;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> start;
    //cout << "start:" << start << endl;
    long res = getSteps(start);
    //out << "res:" << res << endl;
    nt++;
    cout << "Case #" << nt << ": ";
    if (res == -1) cout << "INSOMNIA"; else cout << res;
    cout << endl;
  }
  /*
  for (int i = 0; i <= N; i++) {
    long res = getSteps(i);
    nt++;
    cout << "Case #" << nt << ": ";
    if (res == -1) cout << "INSOMNIA"; else cout << res;
    cout << endl;
  }*/
  return 0;
}
