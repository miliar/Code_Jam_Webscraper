// 08.04.2016
//
// ERROR

/*


*/

# include <cstdio>
# include <cmath>
# include <cstring>

# define isDigit(x) ((x) >= 'A' && (x) <= 'Z')
# define isdigit(x) ((x) >= 'a' && (x) <= 'z')
# define convert(x) ( isdigit (x) ? (x)-'a'+'A' : (x)-'A'+'a' )

# define REV(c) ( (c) == '-' ? '+' : '-' )


# define TRR_JUDGE

//# define TRR_DEBUG


const int N = 110;

int n, m, k, i, j, t, r;
int a, b;
char s [N];

void Reverse (int mm)
{
   for ( int i=0, j=mm; i < j; i++, j-- )
   {
      char t = REV (s [i]);
		s [i] = REV (s [j]);
		s [j] = t;
   }
   if ( mm % 2 == 0 )
      s [mm/2] = REV (s [mm/2]);
}

int main ()
{
# ifdef TRR_JUDGE
   freopen ("B.txt", "r", stdin);
   freopen ("B.out", "w", stdout);
# endif

   scanf ("%d\n", &t);

   for ( int ii=1; ii <= t; ii++ )
   {
      scanf ("%s\n", s);

      m = strlen (s);

# ifdef TRR_DEBUG
printf ("\nlen=%d s=<%s>\n", m, s);
# endif

      k = 0;
      for ( int j=m-1, i; j >= 0; j-- )
         if ( s [j] == '-' )
         {
            if ( s [0] == '+' )
            {
			   for ( i=0; s [i] == '+'; i++ )
			      s [i] = '-';
               k++;
            }
            Reverse (j);
            k++;

# ifdef TRR_DEBUG
printf ("%d) k=%d s=<%s>\n", m, k, s);
# endif
         }

# ifdef TRR_DEBUG
//printf ("len=%d s=<%s>\n", m, s);
# endif

      printf ("Case #%d: %d\n", ii, k);
   }

   return 0;
}
