#include<iostream>
#include<string.h>
#include<math.h>
#include<stdio.h>
using namespace std;
int main(){
    int T,A,B,i,j,k,count;
    bool isSqrt,isFair;
    char num[100];
    cin>>T;
    int result[T];
    for(i = 0; i < T; i++){
        cin>>A>>B;
        count = 0; 
        for(j = A;j <= B; j++){
            isSqrt = false;
            isFair = true;
            if(sqrt(j) == (double)(int)sqrt(j))
               isSqrt = true;
            sprintf(num,"%d",j);
            for(k = 0; k < strlen(num);k++){
                if(num[k] != num[strlen(num)-k-1]){
                    isFair = false;
                    break;
                }
            }
            sprintf(num,"%d",(int)sqrt(j));
            for(k = 0; k < strlen(num);k++){
                if(num[k] != num[strlen(num)-k-1]){
                    isFair = false;
                    break;
                }
            }

            if(isSqrt && isFair){
                count ++;
            }
        }
        result[i] = count;
    }
    for(i = 0; i < T; i++){
        cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
}
