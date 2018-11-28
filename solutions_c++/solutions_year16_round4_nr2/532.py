#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int N, K;
    cin >> N >> K;
    vector<double> p(N);
    for (int i=0;i<N;i++) {
      cin >> p[i];
    }

    sort(p.begin(), p.end());

    int D = N-K;
    double largest = 0;
    for (int x1=0;x1<=K;x1++) {
      int x2 = x1+D;

      vector<double> pp(N+1,0);

      pp[0] = 1;

      for (int i=0;i<N;i++) {
        if (x1 <= i && i < x2) continue;
        for (int j=N;j>0;j--) {
          pp[j] = p[i] * pp[j-1] + (1-p[i]) * pp[j];
        }
        pp[0] = (1-p[i])*pp[0];
      }

      largest = max(largest, pp[K/2]);
    }
    printf("Case #%d: %.10f\n", t, largest);
    /*largest = 0;

    vector<bool> choose(N,true);
    for (int i=0;i<D;i++) choose[i] = false;

    do {
      vector<double> pp(N+1,0);
      pp[0] = 1;
      for (int i=0;i<N;i++) {
        if (!choose[i]) continue;
        for (int j=N;j>0;j--) {
          pp[j] = p[i] * pp[j-1] + (1-p[i]) * pp[j];
        }
        pp[0] = (1-p[i])*pp[0];
      }

      largest = max(largest, pp[K/2]);
    } while (next_permutation(choose.begin(), choose.end()));

    printf("Case #%d: %.10f\n", t, largest);
    do {
      vector<double> pp(N+1,0);
      pp[0] = 1;
      for (int i=0;i<N;i++) {
        if (!choose[i]) continue;
        for (int j=N;j>0;j--) {
          pp[j] = p[i] * pp[j-1] + (1-p[i]) * pp[j];
        }
        pp[0] = (1-p[i])*pp[0];
      }
      if (pp[K/2] == largest) {
        for (int i=0;i<N;i++) {
          if (!choose[i]) continue;
          cout << p[i] << " ";
        }
        cout << endl;
        break;
      }
    } while (next_permutation(choose.begin(), choose.end()));*/
  }

}
    /*for (int x1=0;x1<K-1;x1++) {
      int x2 = x1+D+1;
      for (int allow = x1; allow < x2; allow++) {
        vector<double> pp(N+1,0);

        pp[0] = 1;

        for (int i=0;i<N;i++) {
          if (i != allow) {
            if (x1 <= i && i < x2) continue;
          }
          for (int j=N;j>0;j--) {
            pp[j] = p[i] * pp[j-1] + (1-p[i]) * pp[j];
          }
          pp[0] = (1-p[i])*pp[0];
        }
        if (pp[K/2] > largest) {
          cout << "!!!!!!!!!!" << endl;
        }
        largest = max(largest, pp[K/2]);
      }
    }*/
