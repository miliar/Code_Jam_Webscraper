#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>

long long a[100];

int main() {
    a[1] = 0LL;
    a[2] = 1LL;
    a[3] = 2LL;
    a[4] = 3LL;
    a[5] = 11LL;
    a[6] = 22LL;
    a[7] = 101LL;
    a[8] = 111LL;
    a[9] = 121LL;
    a[10] = 202LL;
    a[11] = 212LL;
    a[12] = 1001LL;
    a[13] = 1111LL;
    a[14] = 2002LL;
    a[15] = 10001LL;
    a[16] = 10101LL;
    a[17] = 10201LL;
    a[18] = 11011LL;
    a[19] = 11111LL;
    a[20] = 11211LL;
    a[21] = 20002LL;
    a[22] = 20102LL;
    a[23] = 100001LL;
    a[24] = 101101LL;
    a[25] = 110011LL;
    a[26] = 111111LL;
    a[27] = 200002LL;
    a[28] = 1000001LL;
    a[29] = 1001001LL;
    a[30] = 1002001LL;
    a[31] = 1010101LL;
    a[32] = 1011101LL;
    a[33] = 1012101LL;
    a[34] = 1100011LL;
    a[35] = 1101011LL;
    a[36] = 1102011LL;
    a[37] = 1110111LL;
    a[38] = 1111111LL;
    a[39] = 2000002LL;
    a[40] = 2001002LL;
    for ( int i = 1;i <= 40;++i )
        a[i] = a[i] * a[i];
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        long long A, B;
        int ans = 0;
        scanf ( "%lld%lld", &A, &B );
        for ( int i = 1;i <= 40;++i )
            if ( a[i] >= A && a[i] <= B )
                ++ans;
        printf ( "Case #%d: %d\n", t, ans );
    }
    return 0;
}