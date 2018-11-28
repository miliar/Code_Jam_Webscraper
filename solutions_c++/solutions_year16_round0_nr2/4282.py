//
// Created by 강경완 on 16. 4. 9..
//

#include <iostream>

using namespace std;
char cake[200] = {0,};

int how(){
    int num = strlen(cake);
    for(int i=num-1; i != -1; i--){
        if(cake[i] == '-'){
            return i;
        }
    }
}

void change(int n){
    int num = strlen(cake);
    for(int i=0; i<=n; i++){
        if(cake[i] == '-')
            cake[i] = '+';
        else if(cake[i] == '+')
            cake[i] = '-';
        else
            printf("Error");
    }
}

bool check(){
    int num = strlen(cake);
    for(int i=0; i<num; i++){
       if(cake[i] == '-')
           return false;
    }
    return true;
}

int main(){

    int n = 0;


    scanf("%d", &n);

    for(int i=0; i<n; i++){

        scanf("%s", cake);
        int num = 0;
        while(true){
            int t = how();
            if(check())
                break;
            change(t);
            num++;
        }
        printf("Case #%d: %d\n",i+1, num);
    }
}
