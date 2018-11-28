#include<stdio.h>
#include <math.h>

int isPal(int n){

    int temp = n;
    int reverse = 0;
       while( temp != 0 )
       {
          reverse = reverse * 10;
          reverse = reverse + temp%10;
          temp = temp/10;
       }
       if ( n == reverse )
          return 1;
       else
          return 0;

}

int main(){

    int test;

    freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);

    scanf("%d",&test);

    for(int caseN=0;caseN<test;caseN++){
        int low,high;
        int count = 0;
        scanf("%d%d",&low,&high);

        for(int i=low;i<=high;i++){
            //printf("%d  ",ceil(sqrt(i)));
            float s = sqrt(i);
            if(isPal(i) && (ceil(s) - s) < 0.000001 && isPal(ceil(sqrt(i)))){
                count++;
            }
        }

        printf("Case #%d: %d\n",caseN+1,count);
    }

}
