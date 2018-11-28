#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <sstream>
#include <fstream>

#include <cstdio>
#include <cmath>

int main(void)
{
    std::ifstream input  ("/Users/nitendra/Desktop/pubmatic/input1");
    short T;
    std::string str;
    short S;
    
    input>>T;
    int cnt = 1;
    while (T--)
    {
        input>>S>>str;
        
        if (str.length() == 1)
        {
            if (std::atoi(str.c_str()) == 0)
            {
                std::cout<<"Case #"<<cnt<<": "<<1<<std::endl;
            }
            else
                std::cout<<"Case #"<<cnt<<": "<<0<<std::endl;
        }
        else
        {
        
            int required = 0;
            int standing = std::atoi(str.substr(0,1).c_str());
            for (int i=1; i<str.length(); ++i)
            {
                //std::cout<<standing<<" "<<required<<" "<<i<<std::endl;
                if (standing<i)
                {
                    ++required;
                    ++standing;
                }
            
            
                int x= std::atoi(str.substr(i,1).c_str());
                standing +=x;
            }
        
        
            std::cout<<"Case #"<<cnt<<": "<<required<<std::endl;
        }
        ++cnt;
    }
    
    
    return 0;
}

