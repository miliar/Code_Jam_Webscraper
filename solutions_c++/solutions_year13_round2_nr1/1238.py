#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>

static const int kMotesSize = 100;

int compare(const void* p1, const void* p2) {
  return *static_cast<const int*>(p1) - *static_cast<const int*>(p2);
}

int solve(long a, int n, int motes[]) {

  // Consume motes in the best order possible.
  qsort(motes, n, sizeof(int), compare);

  int i = 0;
  int addedMotes = 0;
  int removedMotes = 0;
  int answer = n;

  do {

    // Find first mote we cannot consume.
    while (i < n && motes[i] < a) {
      a += motes[i++];
    }

    // How many do we need to delete?
    removedMotes = n - i;
    // printf("a = %ld, i = %d, removedMotes = %d\n", a, i, removedMotes);

    int newAnswer = removedMotes + addedMotes;
    answer = std::min(answer, newAnswer);
    // if (newAnswer >= answer) {
    //   break;
    // }
    // answer = newAnswer;

    if (a == 1) {
      break;  // a cannot grow
    }

    // Try again adding one more mote.
    a += a - 1;
    ++addedMotes;
  } while (removedMotes > 0);

  return answer;
}

int main(int argc, char* argv[]) {
  int t;
  std::cin >> t;

  for (int testCase = 1; testCase <= t; ++testCase) {
    long a;
    int n;
    std::cin >> a >> n;

    int motes[kMotesSize];
    for (int i = 0; i < n; ++i) {
      std::cin >> motes[i];
    }

    printf("Case #%d: %d\n", testCase, solve(a, n, motes));
  }
  return 0;
}
