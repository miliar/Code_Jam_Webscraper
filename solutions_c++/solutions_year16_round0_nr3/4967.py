//
//  main.cpp
//  codejam
//
//  Created by Kevin Hon on 9/4/2016.
//  Copyright © 2016年 aaa. All rights reserved.
//

#include <iostream>
#include <math.h>

__uint64_t arrToBase(bool arr[], int arrLen, int base){
    __uint64_t sum=0;
    
    for (int i=0; i<arrLen; i++){
        if (arr[i]) {
            sum += pow(base, i);
        }
    }
    
    
    return sum;
}

__uint64_t getFactor(__uint64_t value){
    __uint64_t factor = pow(value, 0.5);
    
    while (value%factor > 0){
        factor--;
    }
    
    return factor;
}

bool* nextCoin(bool arr[], int length){
    bool value = false;
    for (int i=0; i<length && !value; i++) {
        arr[i] = !arr[i];
        value = arr[i];
    }
    
    return arr;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int numberOfCase = 0;
    
    std::string inputSeq = "";
    
    //std::cout<<"case:";
    std::cin >> numberOfCase;
    for (int i=0; i<numberOfCase; i++){
        
        __uint64_t value = 0;
        int length = 0;
        int noOfLine = 0;
        
        //std::cout<<"number:";
        std::cin >> length;
        std::cin >> noOfLine;
        
        //init coin
        bool *coinArr = new bool[length];
        for (int j=0; j<length; j++) {
            coinArr[j] = false;
        }
        coinArr[0]=true;
        coinArr[length-1]=true;
        
        __uint64_t resultset[] = {0,0,0,0,0,0,0,0,0};
        
        
        std::cout << "Case #" << i+1 << ": " << std::endl;
        
        //find the first noOfLine value
        for (int j=0; j<noOfLine; j++){
            bool valid = true;
            
            for (int k=0; k<9; k++) {
                resultset[k] = arrToBase(coinArr, length, k+2);
                resultset[k] = getFactor(resultset[k]);
                
                if (resultset[k] == 1){
                    valid = false;
                    break;
                }
                
            }
            
            if (valid && resultset[0] && resultset[length-1]) {
                for (int k=length-1; k>=0; k--) {
                    if (coinArr[k])
                        std::cout << 1;
                    else
                        std::cout << 0;
                }
                
                std::cout << " ";
                
                for (int k=0; k<9; k++) {
                    std::cout << resultset[k] << " ";
                }
                
                std::cout << std::endl;
                
            }else{
                j--;
            }
            
            //gen next value
            coinArr = nextCoin(coinArr, length);
            coinArr = nextCoin(coinArr, length);
            
        }
        
        
        
        
        
    }
    return 0;
}
               


