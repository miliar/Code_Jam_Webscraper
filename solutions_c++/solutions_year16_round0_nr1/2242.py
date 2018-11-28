//
//  main.cpp
//  code-jam
//
//  Created by Ryan on 4/9/16.
//  Copyright © 2016 Ryan. All rights reserved.
//

#include <iostream>

int arr[10];

void arrIni(){
    for(int i=0; i<10; i++){
        arr[i]=0;
    }
}
void insert(int x){
    int ge;
    int res;
    res = x;
    while(res!=0){
        ge = res%10;
        arr[ge] = 1;
        res /= 10;
    }
}
bool finish(){
    for(int i=0; i<10; i++){
        if(arr[i]==0) return false;
    }
    return true;
}
int main(int argc, const char * argv[]) {
    // insert code here...
    
    int T;
    int N;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        arrIni();
        scanf("%d", &N);
        if(N==0){
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        int j=0;
        while(finish()==0){
            j++;
            insert(j*N);
        }
        printf("Case #%d: %d\n", i+1, j*N);
    }
    return 0;
}


