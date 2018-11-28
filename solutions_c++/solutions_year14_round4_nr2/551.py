#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef long long lol;

int N;
int A[1009];

int myinv[1009];
int alinv[1009];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input & init
    scanf("%d", &N);
    int M = 0, argmax = -1;
    for (int i = 0; i < N; ++i) {
      scanf("%d", &A[i]);
      if (M < A[i]) {
        M = A[i];
        argmax = i;
      }
      myinv[i] = 0;
      alinv[i] = 0;
    }
    
    // count inversions
    for (int i = 0; i < argmax; ++i) {
      for (int j = 0; j < i; ++j)
        if (A[j] > A[i]) myinv[i]++;
      for (int j = i + 1; j < argmax; ++j)
        if (A[j] < A[i]) myinv[i]++;
      for (int j = argmax + 1; j < N; ++j)
        if (A[j] > A[i]) alinv[i]++;
    }
    for (int i = argmax + 1; i < N; ++i) {
      for (int j = 0; j < argmax; ++j)
        if (A[j] > A[i]) alinv[i]++;
      for (int j = argmax + 1; j < i; ++j)
        if (A[j] < A[i]) myinv[i]++;
      for (int j = i + 1; j < N; ++j)
        if (A[j] > A[i]) myinv[i]++;
    }
    
    // calculate total
    int total = 0;
    for (int i = 0; i < N; ++i)
      if (i != argmax) {
        //printf("%d (%d) : myinv = %d; alinv = %d; add %d\n", i, A[i], myinv[i], alinv[i], min(myinv[i], alinv[i] + abs(i - argmax)));
        if (myinv[i] < alinv[i] + abs(i - argmax)) {
          total += myinv[i]; // double count
        }
        else {
          total += 2 * (alinv[i] + abs(i - argmax)) - myinv[i];
        }
      }
    
    // output
    printf("Case #%d: %d\n", Ti, total / 2);
  }
  return 0;
}