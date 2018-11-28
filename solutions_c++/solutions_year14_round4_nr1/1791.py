#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
   int nTests;
   cin >> nTests;
   for (int test=0; test<nTests; test++) {
      cerr << test << endl;
      std::vector<int> a;
      int n;
      int x;
      cin >> n;
      cin >> x;
      for (int i=0; i<n; i++) {
          int w;
          cin >> w;
          a.push_back(w);
      }
      sort(a.begin(), a.end());
      int ans = 0;
      int j = n-1;
      int i=0;
      while (i<j) {
          while ((a[i] + a[j] > x) && (j>i)) {
              ans++;
              j--;
          }
          if ((j>i) && (a[i] + a[j] <=x)) {
             ans++;
             j--;
             i++;
          } else break;
      }
      if (i == j) ans++;
      else if (i != j+1) {
        cerr << "i!=j+1" << endl;
        return 1;
      }
      cout << "Case #" << test+1 << ": " << ans << endl;
   }
}