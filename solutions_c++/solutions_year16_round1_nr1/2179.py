#include <stdio.h>
#include <string.h>

void run(){
    char letter[1200];
    char output[2100];
    int back = 1001;
    int front = 999;
    int test = 0;
    scanf(" %s", letter);
    int length = strlen(letter);
    output[1000] = letter[0] ;
    //printf("Main %c\n", letter[0]);
    for(int i = 1; i < length; i++){
        test = 0;
        for(int j = 1000; j > front; j--){
            if(letter[i] < output[j]){
                test = 1;
                break;
            }
        }
        if(test){
            output[back++] = letter[i];
        }else{
            output[front--] = letter[i];
        }
    }
    output[back++] = 0;
    printf("%s\n", &output[front+1]);
}

int main(){
    int T;
    scanf(" %d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        run();
    }
}
