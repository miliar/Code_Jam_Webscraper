//
//  main.cpp
//  [Codejam]CountingSheep
//
//  Created by 장형원 on 2016. 4. 9..
//  Copyright © 2016년 jhw. All rights reserved.
//

#include <iostream>
#include <set>

unsigned int T;
unsigned int N;

std::set<int> s;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cin >> T;
    
    unsigned int test = T;
    
    while(T)
    {
        std::cin >> N;
        unsigned int num = N;
        
        if(N == 0)
        {
            std::cout << "Case #" << test - T + 1 << ": " << "INSOMNIA" << std::endl;
            T = T - 1;
            continue;
        }
        
        unsigned int k = 1;
        while(1)
        {
            unsigned int i = 1;
            
            while(num/i)
            {
                s.insert((num % (i*10))/i);
                
                i *= 10;
            }
            
            if(s.size() == 10)
                break;
            
            k = k + 1;
            num= N * k;
        }
        
        std::cout << "Case #" << test - T + 1 << ": " << num << std::endl;
        s.clear();
        T = T - 1;
    }
    
    return 0;
}
