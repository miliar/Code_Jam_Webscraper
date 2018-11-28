#include <stdio.h>
#include <time.h>

void swap(char&a, char &b){
    char tmp = a;
    a = b;
    b = tmp;
}
char flip(char a){
    return a == '+'?'-':'+';
}
void run(){
    int count = 0;
    char input[101];
    int length;
    scanf(" %s", input);
    for(length = 0; input[length]; length++);
    for(length = length - 1; input[length] == '+'; length--); 
    while(length != -1){
        int l;
        if(input[0] == '-'){
            for(int i = 0; i < (length) / 2 + 1; i++){
                input[i] = flip(input[i]);
                input[length - i] = flip(input[length-i]);
                swap(input[i], input[length-i]);
            }
            if((length & 1) == 0) input[length/2] = flip(input[length / 2]);
            for(length = length; input[length] == '+'; length--);
        }else{
            for(l = 0; input[l] == '+'; l++){
            }
            for(int i = 0; i < l; i++){
                input[i] = flip(input[i]);
            }
            //if( l == 1 ) input[0] = flip(input[0]);
        }
        count++;
    }
    printf("%d\n", count);
}
int main(){
    int T;
    scanf(" %d", &T);
    for(int i = 1; i <= T; ++i){
        printf("Case #%d: ", i);
        run();
    }
}
