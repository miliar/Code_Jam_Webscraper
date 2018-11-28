#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main() {
   int T, N, MAX = 99999;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      cin >> N;
      if (N == 0) {
         cout << "Case #" << t << ": INSOMNIA" << endl;
         continue;
      }
      map<int,int> tracks;
      int n, f = 1;
      while (f < MAX) {
         n = f * N;
         while (n > 0) {
            tracks[n % 10] = 1;
            n /= 10;
         }
         //printf("f x N = %d x %d = %d | #tracks = %d\n", f, N, f * N, tracks.size());
         if (tracks.size() == 10) {
            //cout << N << " x " << f << " = " << (f * N) << endl;
            cout << "Case #" << t << ": " << (f * N) << endl;
            break;
         }
         ++f;
      }
   }
   return 0;
}