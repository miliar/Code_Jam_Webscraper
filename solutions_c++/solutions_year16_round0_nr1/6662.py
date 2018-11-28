//
//  main.cpp
//  codejam
//
//  Created by Kevin Hon on 9/4/2016.
//  Copyright © 2016年 aaa. All rights reserved.
//

#include <iostream>
#include <math.h>

int sumOfArr(int arr[10]){
    int sum=0;
    
    for (int i=0; i<10; i++)
        sum += arr[i];
    
    
    return sum;
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
    __uint64_t value = 0;
    int counter = 0;
    
    int numberOfCase = 0;
    unsigned long input = 0;
    
    //std::cout<<"case:";
    std::cin >> numberOfCase;
    for (int i=0; i<numberOfCase; i++){
        int digitCheck[] = {0,0,0,0,0,0,0,0,0,0};
        //std::cout<<"number:";
        std::cin >> input;
        value = 0;
        counter=0;
        
        std::cout << "Case #" << i+1<< ": ";
        
        if (input == 0){
            std::cout <<"INSOMNIA"<<std::endl;
            continue;
        }
        
        while (sumOfArr(digitCheck) <10){
            value += input;
            counter++;

            __uint64_t tmp = value;
            while (log(tmp) >=0) {
                digitCheck[tmp%10] = 1;
                tmp /= 10;
            }
        }
        
        std::cout << value << std::endl;
        
        
    }
    return 0;
}
               


