//
//  main.cpp
//  [Codejam]CountingSheep
//
//  Created by 장형원 on 2016. 4. 9..
//  Copyright © 2016년 jhw. All rights reserved.
//

#include <iostream>
#include <string>
#include <cmath>

unsigned int T;
unsigned int N;
unsigned int J;

unsigned int retNtd(unsigned long num)
{
    unsigned int i;
    
    if(num == 2 || num == 3)
        return 0;
    else if(num % 2 == 0)
        return 2;
    else
    {
        for(i = 3; i <= sqrt((double)num); i = i + 2)
        {
            if(num % i == 0)
                return i;
        }
    }
    
    return 0;
}

unsigned long convertBaseK(unsigned int num, unsigned long k)
{
    unsigned long convNum = 1;
    unsigned int bitFlg = 1 << 1;
    unsigned long base = k;
    
    for(unsigned int count = 2; count <= N; count++)
    {
        if((num & bitFlg) != 0)
            convNum = convNum + k;
        
        bitFlg = bitFlg << 1;
        k = k * base;
    }
    
    return convNum;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cin >> T;
    
    unsigned int test = T;
    
    while(T)
    {
        std::cin >> N >> J;
        unsigned int i;
        
        unsigned int start = (1 << (N-1)) + 1;
        unsigned int end = 1;
        for(i = 1; i <= N-1; i++)
        {
            end = (end << 1) + 1;
        }
        
        unsigned int num = start;
        
        unsigned int inc = 0;
        
        std::cout << "Case #" << test - T + 1 << ":" << std::endl;
        
        while((J > 0) && (num != end))
        {
            unsigned int ntd[9];
            
            bool isCodeJam = true;
            
            for(i = 2; i <= 10; i++)
            {
                unsigned int x = retNtd(convertBaseK(num, i));
                
                if(x == 0)
                {
                    isCodeJam = false;
                    break;
                }
                else
                {
                    ntd[i-2] = x;
                }
                
            }
            
            if(isCodeJam)
            {
                std::cout << convertBaseK(num, 10) << " ";
                for(i = 0; i < 9; i++)
                    std::cout << ntd[i] << " ";
                std::cout << std::endl;
                J = J - 1;
            }
            
            inc = inc + 1;
            num = start + (inc << 1);
        }
        
        
        T = T - 1;
    }
    
    return 0;
}
