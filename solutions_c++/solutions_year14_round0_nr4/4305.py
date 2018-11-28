#include <cstdio>
#include <algorithm>

using namespace std;

double A[1005], B[1005], B2[1005];

int main()
{
    freopen( "D-large.in", "r", stdin );
    freopen( "outputwar.txt", "w", stdout );
    int T, count = 1;
    scanf( "%d", &T );
    while( T-- )
    {
           int N, ans1=0, ans2=0;
           scanf( "%d", &N );
           for( int i=0; i<N; i++ )
                scanf( "%lf", &A[i] );
           for( int i=0; i<N; i++ )
           {
                scanf( "%lf", &B[i] );
                B2[i] = B[i];
           }   
           
           sort(A, A+N);
           sort(B, B+N);  
           for( int i=N-1; i>=0; i-- )
           {
               for( int j=N-1; j>=0; j-- )
               {
                    if( A[i] > B[j] && B[j]!=-1 )
                    {
                        ans1++;
                        B[j] = -1;
                        break;     
                    }
               } 
           }
           
           for( int i=N-1; i>=0; i-- )
           {
               for( int j=N-1; j>=0; j-- )
               {
                    if( A[i] < B2[j] && B2[j]!=-1 )
                    {
                        ans2++;
                        B2[j] = -1;
                        break;     
                    }
               } 
           }
           
           printf( "Case #%d: %d %d\n", count++, ans1, N-ans2 );
    }
}
