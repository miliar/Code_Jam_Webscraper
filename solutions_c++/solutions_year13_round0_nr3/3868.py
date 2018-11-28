#include <stdio.h>
#include <string>

int main()
{
    int T;
    scanf("%d",&T);

    for(int t=1;t<=T;t++){
        int A,B;

        scanf("%d%d",&A,&B);

        int sum =0;

        if(A<=1 && 1<=B)
            sum++;
        if(A<=4 && 4<=B)
            sum++;
        if(A<=9 && 9<=B)
            sum++;
        if(A<=121 && 121<=B)
            sum++;
        if(A<=484 && 484<=B)
            sum++;


        printf("Case #%d: %d\n",t,sum);

    }
}
