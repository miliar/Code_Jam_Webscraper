#include<stdio.h>

int main() {
    
    int maxShy, testCases, toInt, total, required;
    char shyPersons[1002] = "\0";
    scanf("%d", &testCases);
    
    for(int i=1; i <= testCases; i++) {
        required = 0;
        total = 0;
        scanf("%d", &maxShy);
        scanf("%s", &shyPersons);
        
        printf("Case #%d: ",i);
        
        for(int j=0; j<=maxShy; j++) {
                toInt = shyPersons[j] - '0';
                //printf("%d", toInt);
                
                if(toInt >0) {
                     //printf("\nToInt is %d Total is %d J is %d\n", toInt, total, j);
                     if(total < j) {
                         required += j - total;
                         total = j;
                     }
                     total += toInt;
                }
                
        }
        
        //printf("\nTotal : %d Required : %d\n", total, required);
        printf("%d\n", required);
    } 
}
