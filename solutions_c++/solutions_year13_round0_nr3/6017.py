#include <stdio.h>
#include <math.h>
#define MAX_SIZE 10000000

int result[MAX_SIZE];

bool is_palin(long long n){
    long long reverseN = 0, incomingN = n;

    while (incomingN){
        reverseN = (reverseN * 10) + incomingN % 10;
        incomingN /= 10;
    }

    if (reverseN == n) return true;
    return false;
}

bool fairAndSquare(int i){
    if ( !is_palin( i ) || !is_palin( (long long)(i*i) ) ) return false;
    return true;
}

int main(){

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tCase, kase, i;

    for (i = 1; i < MAX_SIZE; i++){
        if (fairAndSquare(i)) result[i] = result[i-1] + 1;
        else result[i] = result[i-1];
    }

    scanf ("%d",&tCase);

    for (kase = 1; kase <= tCase; kase++){
        long long a, b;
        scanf ("%lld %lld",&a,&b);
        printf ("Case #%d: %d\n", kase, result[(int)sqrt(b)] - result[(int)ceil(sqrt(a))-1]);
    }

    return 0;
}
