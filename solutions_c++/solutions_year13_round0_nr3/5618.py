/*

    Goodle codejam 2013
    Problem C. Fair and Square

*/

#include <stdio.h>
#include <math.h>
#include <string.h>

FILE *in = fopen("input.in", "r") ;
FILE *out = fopen("input.out", "w") ;

bool check(long long num)
{
    char str[20] ;
    sprintf(str, "%lld", num) ;
    int l = strlen(str) ;
    for(int i=0;i<l/2;i++)
        if( str[i] != str[l-i-1] ) return 0 ;
    return 1 ;
}

int main()
{
    int l, g ;
    long long A, B, ans, i, h ;

    fscanf(in, "%d", &l) ;
    for(g=1;g<=l;g++)
    {
        fscanf(in, "%lld %lld", &A, &B) ;
        ans = 0 ;
        for(i=A;i<=B;i++)
        {
            h = sqrt(i) ;
            if( h*h == i && check(h) && check(i) ) ans ++ ;
        }
        fprintf(out, "Case #%d: %lld\n", g, ans) ;
    }

    return 0;
}
