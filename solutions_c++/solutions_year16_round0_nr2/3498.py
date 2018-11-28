//
//  main.cpp
//  [Codejam]CountingSheep
//
//  Created by 장형원 on 2016. 4. 9..
//  Copyright © 2016년 jhw. All rights reserved.
//

#include <iostream>
#include <string>
#include <set>

unsigned int T;
std::string str;

void flip(std::string &str, int j, char mode)
{
    unsigned int i;
    
    if(mode == '+')
    {
        for(i = 0; i <= j; i++)
            str.at(i) = '-';
    }
    else if(mode == '-')
    {
        for(i = 0; i <= j; i++)
            str.at(i) = '+';
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cin >> T;
    
    unsigned int test = T;
    
    while(T)
    {
        std::cin >> str;
        
        unsigned int i;
        char mode = 0;
        unsigned int trial = 0;
        
        while(i < str.length())
        {
            unsigned int j = 0;
            if(str.at(i) == '+')
            {
                mode = '+';
                j = i + 1;
                while(j < str.length())
                {
                    if(str.at(j) == '-')
                        break;
                    j++;
                }
                
                j = j - 1;
            }
            else if(str.at(i) == '-')
            {
                mode = '-';
                j = i + 1;
                while(j < str.length())
                {
                    if(str.at(j) == '+')
                        break;
                    j++;
                }
                
                j = j - 1;
            }
            
            if(mode == '+' && j+1 == str.length())
                break;
                
            //trial
            trial++;
            flip(str, j, mode);
            
            i = 0;
        }
        
        std::cout << "Case #" << test - T + 1 << ": " << trial << std::endl;
        
        
        T = T - 1;
    }
    
    return 0;
}
