#include <stdio.h>

int check[10];

bool digits(long long M) {
    while (M != 0) {
        check[M%10] = 1;
        M /= 10;
    }
    int sum = 0;
    for (int i=0; i<10; i++) {
        sum += check[i];
    }
    if(sum==10)
        return true;
    else
        return false;
}

int main()
{
    int T,N,i,c;
    long long M;
    scanf("%d", &T);
    for(c=1; c<=T; c++)
    {
        for (i=0;i<10;i++)
            check[i] = 0;
        scanf("%d",&N);
        if (N==0){
            printf("Case #%d: INSOMNIA\n",c);
        }
        else {
            M = N;
            while (digits(M) == false)
                M += N;
            printf("Case #%d: %d\n",c,M);
        }
    }
    return 0;
}
