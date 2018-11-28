// 11.04.2015
//

/*

*/

# include <cstdio>
# include <algorithm>

using namespace std;



# define TRR_JUDGE

const int N = 1010;

int n, m, k, i, j, t, r;
int a, b;
char s [N];

void Print ();

int main ()
{
   freopen ("A.txt", "rt", stdin);
   freopen ("A.out", "wt", stdout);

   scanf ("%d\n", &t);

   for ( int i=1, j; i <= t; i++ )
   {
      scanf ("%d %s\n", &n, s);
      k = 0;
      b = s [0] - '0';
      for ( j=1; j <= n; j++ )
      {
         a = s [j] - '0';
         if ( b < j )
            k += j-b, b = j;
         b += a;
      }

# ifdef TRR_JUDGE
//   printf ("");
# endif

      printf ("Case #%d: %d\n", i, k);
   }

   return 0;
}

