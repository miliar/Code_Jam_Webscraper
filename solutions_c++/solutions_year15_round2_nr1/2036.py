#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int reversal(int n){
    int lenght = (int)(log(n) / log(10)) + 1 , i = 0;
    int rev = 0;
    while(n != 0){
        rev += (n % 10) * (round(pow(10, lenght - 1 - i)));
        n /= 10;
        i++;
    }
    return rev;
}
int main(){
    int T, i, j, N, *cost = (int *)malloc(sizeof(int) * 1000005);
    scanf("%d ", &T);
    cost[1] = 1;
    for (i = 1 ; i <= T ; i++){
        scanf("%d ", &N);
        for (j = 2 ; j <= N ; j++){
            cost[j] = cost[j - 1] + 1;
            if (reversal(j) < j && reversal(reversal(j)) == j)
                if (cost[j - 1] > cost[reversal(j)])
                    cost[j] = cost[reversal(j)] + 1;
        }
        printf("Case #%d: %d\n", i, cost[N]);
    }
    return 0;
}
