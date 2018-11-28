#include <iostream>

#include <string>
#include <algorithm>

using namespace std;

char winner(char c1, char c2) {
   if (c1 == c2) return 0;
   switch (c1) {
      case 'R':
         return c2 == 'P' ? c1 : c2;
      case 'S':
         return c2 == 'R' ? c1 : c2;
      case 'P':
         return c2 == 'S' ? c1 : c2;
   }
   return 0;
}

bool sim(int N, string P) {
   for (int r = 1; r <= N; ++r) {
      string rem;
      for (int i = 1; i < (int) P.size(); i += 2) {
         char c = winner(P[i-1], P[i]);
         if (c == 0) return false;
         rem += c;
      }
      P = rem;
   }
   return true;
}

string solve(int N, int R, int P, int S) {
   string T = string(R, 'R') + string(P, 'P') + string(S, 'S');
   sort(T.begin(), T.end());
   do {
      if (sim(N, T)) {
         return T;
      }
   } while (next_permutation(T.begin(), T.end()));
   return "IMPOSSIBLE";
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      int N, R, P, S;
      cin >> N >> R >> P >> S;
      string res = solve(N, R, P, S);
      cout << "Case #" << tc << ": " << res << endl;
   }

   return 0;
}
