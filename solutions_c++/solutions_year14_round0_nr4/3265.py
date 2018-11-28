#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int chosenIndex(double val, const vector<double> &a) {
   if (a.size() == 0) {
      fprintf(stderr, "WRONG!!!\n");
      system("pause");
      return 0;
   }
   if (val > a[a.size() - 1]) {
      return 0;
   }
   int poz = 0;
   while (val > a[poz]) {
      poz++;
   }
   return poz;
}

int optimalWar(const int N, vector<double> a, vector<double> b) {
   int wins = 0;
   while (a.size() > 0) {
      while (a.size() > 0 && a[a.size() - 1] > b[b.size() - 1]) {
         a.pop_back();
         b.erase(b.begin());
         wins++;
      }
      if (a.size() == 0) {
         break;
      }
      int pozA = a.size() - 2;
      if (pozA < 0) {
         pozA = 0;
      }
      const int pozB = chosenIndex(a[pozA], b);
      a.erase(a.begin() + pozA);
      b.erase(b.begin() + pozB);
   }
   return wins;
}

int optimalDeceit(const int N, vector<double> a, vector<double> b) {
   int wins = 0;
   while (a.size() > 0) {
      while (a.size() > 0 && a[0] < b[0]) {
         a.erase(a.begin());
         b.pop_back();
      }
      while (a.size() > 0 && a[0] > b[0]) {
         a.erase(a.begin());
         b.erase(b.begin());
         wins++;
      }
   }
   return wins;
}

void Solve() {
   int N;
   scanf("%d", &N);
   vector<double> a(N), b(N);
   for (int i = 0; i < N; i++) {
      scanf("%lf", &a[i]);
   }
   sort(a.begin(), a.end());
   for (int i = 0; i < N; i++) {

      scanf("%lf", &b[i]);
   }
   sort(b.begin(), b.end());
   printf("%d %d\n", optimalDeceit(N, a, b), optimalWar(N, a, b));
}

int main() {
   freopen("data.in", "rb", stdin);
   freopen("data.out", "wb", stdout);
   int tst;
   scanf("%d", &tst);
   for (int i = 1; i <= tst; i++) {
      printf("Case #%d: ", i);
      Solve();
   }
}