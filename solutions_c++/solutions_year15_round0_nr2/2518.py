#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

// Global constants (MUST change for different datasets !!!!!)
const int P_MAX = 1000;

int nextMax(int start, const int* count) {
   for (int i = start; i > 0; --i) if (count[i]) return i;
   return -1;
}

// 1. pick max, compute next, try split max while newMax >= ((1 + max) >> 1)
// 2. if cost down, recursively call work on newMax
int solve(const int max, int* count, int special) {
   int curBest = max + special; if (max <= 3) return curBest;
   int next = nextMax(max - 1, count), newMax, size, result;
   for (int i = 1, j = max >> 1; i <= j; ++i) {
      // try split max into i and (max - i)
      newMax = (next > (max - i)) ? next : (max - i);
      if (max < (newMax + count[max])) continue;
      // realloc pancakes
      size = count[max]; count[max] = 0;
      count[i] += size; count[max - i] += size;
      // recursive call
      result = solve(newMax, count, special + size);
      if (result < curBest) curBest = result;
      // set pancakes back
      count[max] = size;
      count[i] -= size; count[max - i] -= size;
   }
   return curBest;
}

int main() {
   // parse T, the number of cases
   int T; cin >> T; if (T <= 0) return 0;
   // parse each cases, solve it, and keep the result for final output
   int count[1 + P_MAX];
   for (int i = 0; i < T; ++i) {
      int N, temp; cin >> N;
      for (int j = 0; j <= P_MAX; ++j) count[j] = 0;
      for (int j = 0; j < N; ++j) {
         cin >> temp; assert (P_MAX >= temp);
         ++count[temp];
      }
      int result = solve(nextMax(P_MAX, count), count, 0);
      cout << "Case #" << (1 + i) << ": " << result << endl;
   }
   return 0;
}

