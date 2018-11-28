#include <iostream>
#include <stdlib.h>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int solve(int N, int X, vector<int>& s) {
   std::sort (s.begin(), s.end());
   int discs = 0;
   for (int i = s.size() - 1;i >= 0;i--) {
    if (s[i] <= 0) continue;
     int demand = s[i];
     s[i] *= -1;
     for (int j = i - 1;j >= 0;j--) {
       if (s[j] <= 0) continue;
       if (s[j] + demand <= X) {
         s[j] *= -1;
         break;
       }
     }
     discs++;
   }
   return discs;
}

int main(int argc, char* argv[]) {
  int T;
  cin >> T;
  string s;
  for (int t = 0;t < T;t++) {
    int N, X;
    cin >> N >> X;
    vector<int> s;
    for (int i = 0;i < N;i++) { int size; cin >> size; s.push_back(size); }
    int cost = solve(N, X, s);
    std::cout << "Case #" << (t+1) << ": ";
    std::cout << cost;
    std::cout << endl;
  }
  return 0;
}

