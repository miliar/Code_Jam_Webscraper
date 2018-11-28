#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

#define MAX_N (1000000)


typedef uint64_t T;

T prevs[MAX_N+1];
T rec_count;
T reverse(T n) {
  T reversed = 0;
  while (n > 0) {
    reversed = reversed*10 + (n % 10);
    n /= 10;
  }
  //cout << "reversed: " << reversed << "\n";
  return reversed;
}

T solve(T n) {
  //rec_count++;
  //cout << "rec_count " << rec_count << "\n";
  //cout << "n: " << n << ", ";

  //cout << "prevs[n]: " << prevs[n] << ", ";
  if (prevs[n] > 0) {
    return prevs[n];
  }

  if (n == 1) {
    return 1;
  }

  T rev = (n%10 == 0 ? n : reverse(n));
  T prev = solve(n-1);
  prevs[n] = (rev>=n ? prev+1 : min(prev+1, solve(rev)+1));

  return prevs[n];
}

int main() {
  vector<int> result;

  int tests;
  T N;
  cin >> tests;

  for (T i=1; i <= MAX_N; i++) {
    solve(i);
  }
  for (int t=0; t<tests; t++) {
    cin >> N;
    //cout << N << "\n";
    rec_count = 0;
    result.push_back(solve(N));
  }

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i] << "\n";
  }
  return 0;
}
