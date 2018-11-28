#include <cstdio>

using namespace std;

int main() {
   int T, digs[10], n;

   scanf("%d", &T);
   for (int t = 1; t <= T; t++) {
      scanf("%d", &n);
      if (!n) printf("Case #%d: INSOMNIA\n", t);
      else {
         long v = 0; // long. just in case..
         int cnt = 0;
         for (int i = 0; i < 10; i++) digs[i] = 0;
         while (cnt < 10) {
            v += n;
            for (long tmp = v; tmp; tmp/=10)
               cnt+=!(digs[tmp%10]++);
         }
         printf("Case #%d: %ld\n", t, v);
      }
   }
	return 0;
}
