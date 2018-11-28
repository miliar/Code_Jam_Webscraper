#include<iostream> 
using namespace std; 

int main () {
    int cases, tCase = 1, remaining,ctr,digits[10]={0,0,0,0,0,0,0,0,0,0},digit;
    long input,number;  
    scanf("%d", &cases);
    while (tCase <= cases){
          scanf("%ld", &input);
          remaining=10;
          ctr=0;
          if(input == 0 )
                   printf("Case #%d: INSOMNIA\n",tCase);
          else {
               for(int i=0; i<10; i++)
                       digits[i]=0;
               while (remaining >  0){
                     number = input * ++ctr;
                     while(number>0) {
                                     digit=number%10;
                                     number/=10;
                                     if (digits[digit] == 0) {
                                                       digits[digit] = 1;
                                                       remaining --;
                                                       }
                                     }
                     }
                     printf("Case #%d: %ld\n",tCase,input*ctr);
               }
          tCase++;
          }
    return 1;
}
