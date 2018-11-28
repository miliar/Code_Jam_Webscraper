#include <cstdio>
#include <cmath>
#include <cstring>

int palindromo(int a) {
    char number[10];
    sprintf(number,"%d",a);
    int tam = strlen(number);
    int i = 0;
    int eh_pal = 1;
    
    while (i < tam-i-1 && eh_pal) {
        if (number[i] != number[tam-i-1])
            eh_pal = 0;
        i++;
    } 
    
    return eh_pal;
}


int main(int argc, const char *argv[])
{
    int t, a, b, count, lower, upper, caso = 1;
    scanf("%d",&t);
    while (t--) {
        scanf("%d %d",&a,&b);
        count = 0;
        lower = (int) sqrt((double) a);
        upper = (int) sqrt((double) b);
        if (lower*lower < a)
            lower++;
        while (lower <= upper) {
            if (palindromo(lower)) {
                if (palindromo(lower*lower))
                    count++;
            }
            lower++;
        }
        printf("Case #%d: %d\n",caso,count);
        caso++;
    }
    return 0;
}
