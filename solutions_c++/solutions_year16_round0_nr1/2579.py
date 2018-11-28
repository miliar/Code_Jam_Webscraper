#include <stdio.h>
#define MOD_MAX 10000000
#define COUNT_ALL 0b1111111111

int getNumber(int input){
    int output = 0;
    while(input){
        output |= (1 << ((input ) % 10));
        input /= 10;
    }
    return output;
}
int getLength(int input){
    int count = 0;
    while(input){
        count++;
        input /= 10;
    }
    return count;
}
void run(){
    int output = 0;
    int length = 1;
    int value, value2;
    int i;
    scanf("%d", &value2);
    int temp = getLength(value2);
    for(i = 0; i <= temp; i++)
        length *= 10;
    
    for(i = 0; i < length; i++){
        value = (value2 * (i+1) ) % (MOD_MAX);
        output |= getNumber(value);
        if(output == COUNT_ALL) break;
    }
    if(output == COUNT_ALL) printf("%d\n", value);
    else printf("INSOMNIA\n");
}


int main(){
    int T;
    scanf(" %d", &T);
    for(int i = 0; i < T; i++){
        printf("Case #%d: ", i + 1);
        run();
    }
}
