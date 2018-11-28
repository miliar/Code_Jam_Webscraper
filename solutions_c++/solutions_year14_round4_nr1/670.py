#include <iostream>

#include <cstring>

#include <algorithm>
#include <map>

using namespace std;

#define FOREACH(it,c) for(__typeof__((c).begin()) it=(c).begin();it!=(c).end();++it)

int N;
int freq[1000];

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      int X;
      cin >> N >> X;
      memset(freq, 0, sizeof(freq));
      for (int i = 0; i < N; ++i) {
         int s;
         cin >> s;
         ++freq[s];
      }
      int res = freq[X];
      for (int s = X-1; s >= 1; --s) {
         while (freq[s] > 0) {
            --freq[s];
            int t;
            for (t = X - s; t >= 1 && freq[t] <= 0; --t);
            if (t > 0)
               --freq[t];
            ++res;
         }
      }
      cout << "Case #" << tc << ": " << res << endl;
   }

   return 0;
}
