#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;


int T, N, sum, result, num=1;

int main(){
    char str[100000];
    FILE * ip = fopen("/Users/clsrn1581/Downloads/A-large.in", "r");
    
    fscanf(ip, "%d", &T);
    
    while(T--){
        sum = 0;
        result = 0;
        
       fscanf(ip, "%d", &N);
        fscanf(ip, "%s", str);
        
        for(int i = 0 ; i < N+1 ; i++){
            if(sum < i){
                result += i-sum;
                sum = i;
            }
                sum += str[i]-'0';
            
        }
        printf("Case #%d: %d\n", num++ , result);
    }
    return 0;
}