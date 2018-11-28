#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <functional>
#include <string>

using namespace std;

//	Pairs
#define MP make_pair
#define F first
#define S second
typedef pair<int, int> ii;

// Vectors
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;

int cons(char c) { return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u'; }

char s[200];

int main() {
   int T, n;
   //freopen("a.in", "r", stdin);

   s[0] = 0;
   scanf("%d\n", &T);
   for (int t = 1; t <= T; t++) {
      scanf("%s %d\n", s+1, &n);

      int sol = 0;
      int l = strlen(s+1);
      for (int i = 0; i < l; i++)
         for (int j = i; j < l; j++) {
            int cur, c;
            cur = c = 0;

            //for (int k = i+1; k <= j +1 ; k++) printf("%c", s[k]);
            //printf("\n");

            for (int k = i+1; k <= j+1; k++)
               if (cons(s[k]) && cons(s[k-1])) cur++;
               else if (!cons(s[k])) { c = max(c, cur); cur = 0; }
               else if (cons(s[k])) cur = 1;
            c = max(c, cur);

            if ( c >= n ) sol++;
         }
      
      printf("Case #%d: %d\n",t,  sol);
   }
   return 0;
}
