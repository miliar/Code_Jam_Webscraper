#include <cstdio>
#include <cstring>
#define N 100000000000000LL
long long int v[100], pos;
int ispal( long long int n ) {
    char nn[20];
    sprintf(nn, "%lld", n);
    int i=0, k=strlen(nn) - 1;
    while( i < k ) {
        if( nn[i] != nn[k] ) return 0;
        i++; k--;
    }
    return 1;
}
void f() {
    pos = 0;
    long long int n = 1LL;
    while( n*n <= N ) {
        if( n%10LL != 0LL && ispal(n) && ispal(n*n) ) v[pos++] = n*n;
        n++;
    }
}
int main() {
    int t, cnt, i;
    long long int a, b;
    f();
    /*for( int i=0 ; i<pos ; i++ ) printf("%lld ", v[i]);
    printf("\n");
    */
    scanf("%d",&t);
    for( int casos=1 ; casos<=t ; casos++ ) {
        cnt = 0;
        scanf("%lld %lld", &a, &b);
        i = 0;
        while( i < pos && v[i] < a ) i++;
        while( i < pos && v[i] <= b ) {
            cnt++;
            i++;
        }
        printf("Case #%d: %d\n", casos, cnt);
    } 
    return 0;
}
