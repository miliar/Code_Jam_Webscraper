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



int main( int argc, char* argv[] )
{
    int n_cases;
    int number;
    int used, tmp, accumulated;
    
    scanf("%d", &n_cases);
    
    for( int i_case = 0; i_case < n_cases; i_case++ ) {
        scanf("%d", &number); 
        
        if( number == 0 ) {
            printf("Case #%d: INSOMNIA\n", i_case+1);
            continue;
        }
        
        used = 0;
        accumulated = 0;
        
        while( !(used == (1 << 10) - 1)) {
            accumulated += number;
            tmp = accumulated; 
            while(tmp) {
                used |= 1 << (tmp%10);
                tmp /= 10;
            }
        }
        
        printf("Case #%d: %d\n", i_case+1, accumulated);
    }
    
    return 0;
}