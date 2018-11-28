/****************************************************/
/*                                                  */  
/*  Fran Muñoz                                      */
/*  email: fran.mzy@gmail.com                       */
/*  UVA user: franmzy                               */   
/*  Linkedin: https://www.linkedin.com/in/franmzy   */
/*                                                  */
/****************************************************/

#include <bits/stdc++.h>
using namespace std;

#define pb         push_back
#define mp         make_pair
#define LL         long long
#define ULL        unsigned long long
#define inf        1<<30
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)
#define DEBIN(n)   printf("GET IN: %d\n", n);
#define DEBOUT(n)   printf("GET OUT: %d\n", n);
#define UI          unsigned int

typedef pair<int, int> ii;
typedef vector<ii> vii;

#define MAX_LONG_PAN 500

void trim( char *str )
{
	char *inicio = str;
	char *final;

	while( isspace( *inicio ) ) inicio++;

	final = str;

	while( *final != '\0' ) final++;
	final--;
	while( final >= inicio && isspace( *final ) ) final--;

	while( inicio <= final ) *str++ = *inicio++;
	*str = '\0';
}

int main( int argc, char* argv[] )
{
    int n_cases;
    int n_flips;
    char pancake, last_pancake;
    
    char buffer[MAX_LONG_PAN+5];
    
    scanf("%d\n", &n_cases);
    
    for( int i_case = 0; i_case < n_cases; i_case++ ) {
        
        fgets( buffer, MAX_LONG_PAN, stdin );
		trim( buffer );

		stringstream ss( buffer );
		ss >> last_pancake ;
		
		n_flips = 0;
		while( ss >> pancake ) {
		    if( pancake != last_pancake ) n_flips++;
		    last_pancake = pancake;
		}
		if( last_pancake == '-' )
		    n_flips++;
        
        printf("Case #%d: %d\n", i_case+1, n_flips);
    }
    
    return 0;
}