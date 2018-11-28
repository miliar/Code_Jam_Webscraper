#include<bits/stdc++.h>
using namespace std;

int ar[20], cnt;
int main()
{

    freopen("codeJamIn.txt", "r", stdin);
        freopen("codeJamOut.txt", "w", stdout);

    int cs, csno, i;
    long long n, nn, tmp;

    scanf("%d", &cs);

    for(csno =1; csno <= cs; csno++){
        scanf(" %lld",  &n);

        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", csno);
            continue;
        }
        for( i = 0 ; i <= 9; i++){
            ar[i] = 0;
        }
        cnt = 0;
        nn = n;

        while( cnt != 10){
            tmp = nn;
            while(tmp != 0){
                if (ar[tmp % 10 ] == 0)
                {
                    cnt++;
                    ar[tmp % 10 ] = 1;
                }
                tmp /= 10;
            }
            nn += n;

        }
        printf("Case #%d: %lld\n", csno, nn - n);

    }

    return 0;

}
