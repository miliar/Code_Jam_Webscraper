#include <stdlib.h>
#include <iostream>

using namespace std;

void solve(long long N)
{
  if (N == 0) {
    cout << "INSOMNIA";
    return;
  }

  bool see[10];
  for (int i = 0; i < 10; i++) {
    see[i] = false;
  }

  int i = 1;
  while (true)
  {
    long long t = i * N;
    while (t > 0) {
      see[t % 10] = true;
      t /= 10;
    }

    bool done = true;
    for (int j = 0; j < 10; j++) {
      if (!see[j]) {
        done = false;
        break;
      }
    }

    if (done) {
      break;
    }

    i++;
  }
  cout << i * N;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N;
    cin >> N;

    cout << "Case #" << t << ": ";
    solve(N);
    cout << "\n";
  }
}

