//
//  main.cpp
//  [Codejam]CountingSheep
//
//  Created by 장형원 on 2016. 4. 9..
//  Copyright © 2016년 jhw. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>
#include <set>

unsigned int T;
unsigned int C;
unsigned int K;
unsigned int S;

std::map<std::string, std::string> Artwork;

std::string convertTileForm(unsigned int num, unsigned int c)
{
    std::string str;
    
    unsigned int bitFlg = 1;

    for(unsigned int i = 0; i < c; i++)
    {
        if((num & bitFlg) != 0)
            str = "L" + str;
        else
            str = "G" + str;
        
        bitFlg = bitFlg << 1;
    }
    
    return str;
}

std::string makeComplex(std::string org, unsigned int c)
{
    std::string str;
    
    unsigned int bitFlg = 1;
    
    for(unsigned int i = 0; i < org.length(); i++)
    {
        if(org.at(i) == 'G')
        {
            std::string temp;
            for(unsigned int j = 0; j < c; j++)
                temp += "G";
            str = str + temp;
        }
        else if(org.at(i) == 'L')
            str = str + org;
        
        bitFlg = bitFlg << 1;
    }
    
    return str;
}

void makeTile(unsigned int c, unsigned int k)
{
    unsigned int i;
    unsigned int start = 0;
    unsigned int end = 1;
    
    for(i = 1; i < c; i++)
    {
        end = (end << 1) + 1;
    }
    
    std::string originStr;
    std::string complexStr;
    
    for(i = start; i <= end; i++)
    {
        originStr = convertTileForm(i, c);
        complexStr = originStr;
        for(unsigned int j = 1; j < k; j++)
            complexStr = makeComplex(complexStr, c);
        
        Artwork.insert(std::map<std::string, std::string>::value_type(originStr, complexStr));
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cin >> T;
    
    unsigned int test = T;
    
    while(T)
    {
        std::cin >> C >> K >> S;
        
        unsigned int i;
        
        //makeTile(C, K);
        
        std::set<unsigned int> result;
//        std::map<std::string, std::string>::iterator iter;
//        iter = Artwork.begin();
//        
//        for(i = 0; i <iter->second.length(); i++)
//        {
//            while(iter != Artwork.end())
//            {
//                
//                
//                iter++;
//            }
//            
//        }

        if(C == 1)
            result.insert(1);
        else
        {
            for(i = C; i >= 2; i--)
                result.insert(i);
        }
        
        if(K == 1)
        {
            result.insert(1);
        }
        
        std::cout << "Case #" << test - T + 1 << ":";
        if(result.size() > S)
            std::cout << " IMPOSSIBLE" << std::endl;
        else
        {
            std::set<unsigned int>::iterator iter;
            for(iter = result.begin(); iter != result.end(); iter++)
                std::cout << " " << *iter;
            std::cout << std::endl;
        }
        
        //Artwork.clear();
        result.clear();
        T = T - 1;
    }
    
    return 0;
}
