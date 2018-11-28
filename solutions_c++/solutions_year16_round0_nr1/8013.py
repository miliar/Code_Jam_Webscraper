// 08.04.2016
//

/*


*/

# include <stdio.h>
# include <math.h>
# include <string.h>

# define isDigit(x) ((x) >= 'A' && (x) <= 'Z')
# define isdigit(x) ((x) >= 'a' && (x) <= 'z')
# define convert(x) ( isdigit (x) ? (x)-'a'+'A' : (x)-'A'+'a' )



# define TRR_JUDGE



const int N = 10;

int n, m, k, i, j, t, r;
int a, b;
bool d [N];

bool Check ()
{
   bool ok = d [0];
   for ( int j=1; j < 10; j++ )
      ok = ok && d [j];
   return ok;
}

int main ()
{
# ifdef TRR_JUDGE
   freopen ("A.txt", "r", stdin);
   freopen ("A.out", "w", stdout);
# endif

   scanf ("%d\n", &t);

   for ( int ii=1; ii <= t; ii++ )
   {
      scanf ("%d\n", &n);

      if ( n == 0 )
         printf ("Case #%d: INSOMNIA\n", ii);
      else
      {
         for ( int j=0; j <= 9; j++ )
            d [j] = false;

  	 	   int nn = n;
         while ( nn > 0 )
            d [nn%10] = true,
				nn /= 10;

         for ( int j=1; j <= 1000; j++ )
         {
			 	nn = n*j;
            while ( nn > 0 )
               d [nn%10] = true,
	  			   nn /= 10;

            if ( Check () )
            {
               k = n*j; break;
				}
			}

//printf ("n=%d j=%d\n", n, k/n);

         printf ("Case #%d: %d\n", ii, k);
      }
   }

   return 0;
}
