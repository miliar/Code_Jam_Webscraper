# include <stdio.h>


char A[110], B[110] ;
char table[50000][110] ;


int main ()
{
	int T, nCase = 1 ;
	int cnt = 0, cc, i;
	FILE *fin = fopen ("table.in", "r") ;
	while (~scanf ("%s", A))
		strcpy (table[cnt++], A) ;
	fclose (fin) ;
	
	freopen ("C-large-2.in", "r", stdin) ;
	freopen ("out.txt", "w", stdout) ;
	
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%s%s", A, B) ;
		for (i = 0 ; i < cnt ; i++)
		{
			if (cmp(table[i],A)>=0 && cmp(table[i],b)<=0)cc++ ;
			if (cmp(table[i],B) > 0) break ;
			printf ("Case #%d: %d\n", nCase++, cc) ;
		}
	}
}
