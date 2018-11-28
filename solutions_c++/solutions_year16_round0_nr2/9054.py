#include <bits/stdc++.h>
using namespace std;

int position;
int negative;
int number;
int answer;
char arr[1000];

int main(){
    scanf("%d",&number);
    int t = 1;
    while(number-->0){
        scanf("%s",arr);
        int end = -1;
        negative = 0;
        position = 0;
        answer = 0;
        int num = strlen(arr);
        for(int counter = num-1;counter>=0;counter--){
            if(arr[counter] == '-'){
                end = counter;
                break;
            }
        }
        if(arr[0] == '-') negative = 1;
        else position = 1;
        for(int counter = 1;counter<=end;counter++){
            if(arr[counter] == '-' and negative){
            }
            else if(arr[counter] == '-' and position){
                position = 0;
                negative = 1;
                answer++;
            }
            else if(arr[counter] == '+' and negative){
                position = 1;
                negative = 0;
                answer++;
            }
            else if(arr[counter] == '+' and position){

            }
        }
        if(negative) answer++;
        printf("Case #%d: %d\n",(t++),answer);
    }

	return 0;
}
