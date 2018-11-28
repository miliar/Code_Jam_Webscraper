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
    
    int numberOfCase = 0;
    
    std::string inputSeq = "";
    
    //std::cout<<"case:";
    std::cin >> numberOfCase;
    for (int i=0; i<numberOfCase; i++){
        
        //std::cout<<"number:";
        std::cin >> inputSeq;
        
        int counter = 1;
        char sign = inputSeq[0];
        
        for (int i=0; i<inputSeq.length(); i++){
            if (!(inputSeq[i] == sign))
                counter ++;
            
            sign = inputSeq[i];
            
            if (inputSeq.length()-1==i && '+'==sign){
                counter--;
            }
            
        }
        
        
        std::cout << "Case #" << i+1 << ": ";
        std::cout << counter << std::endl;
        
        
    }
    return 0;
}
               


