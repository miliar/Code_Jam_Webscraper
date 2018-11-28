#include <cstdio>

#include <algorithm>

using namespace std;

typedef long long llong;

int N;
int A[1004];
int S[1004];
int P[1004];

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d", &N);
      for (int i = 1; i <= N; ++i) {
         scanf("%d", A+i);
         S[i] = A[i];
      }
      sort(S+1, S+N+1);
      for (int i = 1; i <= N; ++i) {
         int r = lower_bound(S+1, S+N+1, A[i]) - S;
         A[i] = r;
         P[r] = i;
      //   cerr << A[i] << ' ';
      }
      //cerr << endl;

      llong res = 0;
      int L = 1, R = N;
      for (int r = 1; r <= N; ++r) {
         int pos = P[r];
      // fprintf(stderr, "r = %d  pos = %d\n", r, pos);
         if (pos - L < R - pos) {
            for (int i = pos-1; i >= L; --i) {
               int a = A[i];
               A[i+1] = a;
               P[a] = i+1;
               ++res;
            }
            A[L] = r;
            L++;
         }
         else {
            for (int i = pos+1; i <= R; ++i) {
               int a = A[i];
               A[i-1] = a;
               P[a] = i-1;
               ++res;
            }
            A[R] = r;
            R--;
         }
      }
      printf("Case #%d: %lld\n", tc, res);
   }

   return 0;
}
