#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int A, B, K, cnt;

    int t;
    scanf("%d", &t);
    for(int k=1; k<=t; k++){
        scanf("%d %d %d", &A, &B, &K);
        
        cnt = 0;
        for(int i=0; i<A; i++){
            for(int j=0; j<B; j++){
                if( (i&j) < K )
                    cnt++;
            }
        }

        printf("Case #%d: %d\n", k, cnt);
    }

    return 0;
}
