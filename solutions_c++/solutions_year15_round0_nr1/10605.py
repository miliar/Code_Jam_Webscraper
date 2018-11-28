#include "string"
#include "cstdio"
#include "cstring"
#include "cmath"
#include "iostream"
#include "vector"
#include "list"
using namespace std ;

const int maxn = 1000 ;
int s[maxn];
int smax;
int main()
{
    FILE* fp = 0;
    if(0 == ( fp = freopen("A-small-attempt0.out", "w" ,stdout)))
         printf("Cannot open file.\n");
    int T = 0;
    scanf ( "%d" , &T ) ;
    printf("%d\n", T);
    int totalCase = T;
    while ( T -- )
    {
        scanf ( "%d " , &smax) ;
        for (int i = 0 ; i <= smax ; i ++ ){
            // scanf ( "%c" , s+i) ;
            s[i] = getchar()-'0';
        } 
        int total = 0;
        int toInvite = 0;
		for ( int i = 0 ; i <= smax ; i ++ ){
            if(total < i){
                toInvite += i - total;
                total = i + s[i];
            }else{
                total += s[i];
            }
            // printf("%d %d %d %d\n", i, s[i], total, toInvite);
        }
        printf("Case #%d: %d\n", totalCase - T, toInvite );
    }
    fclose(fp);
    return 0 ;
}
