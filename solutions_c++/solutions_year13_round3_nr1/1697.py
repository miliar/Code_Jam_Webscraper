//
//  main.cpp
//  codeJam2013
//
//  Created by Guillaume Derval on 13/04/13.
//  Copyright (c) 2013 Guillaume Derval. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>


int main(int argc, const char * argv[])
{
    std::ifstream finput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/A-small-attempt0.in");
    std::ofstream foutput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/out.out");
    
//#define NORMAL_INPUT
#ifdef NORMAL_INPUT
    std::istream& input = std::cin;
    std::ostream& output = std::cout;
#else
    std::istream& input = finput;
    std::ostream& output = foutput;
#endif
    
    int T;
    input >> T;
    for(int test = 0; test < T; test++)
    {
        std::string name;
        int n;
        input >> name >> n;
        
        bool* consonnes = new bool[name.length()];
        for(int i = 0; i < name.length(); i++)
            if(name.c_str()[i] == 'a' || name.c_str()[i] == 'i' || name.c_str()[i] == 'e' || name.c_str()[i] == 'o' || name.c_str()[i] == 'u')
               consonnes[i] = false;
            else
               consonnes[i] = true;
        
        int count = 0;
        int now = 0;
        for(int i = 0; i < name.length(); i++)
        {
            bool ok = true;
            for(int j = 0; j < n && ok; j++)
            {
                if(i+j >= name.length()) ok = false;
                if(!consonnes[i+j]) ok = false;
            }
            if(ok)
            {
                int first_pos = i;
                count += (name.length()-(first_pos+n)+1)*(first_pos-now+1);
                now = first_pos+1;
            }
        }
        
        output << "Case #" << (test+1) << ": " << count << std::endl;
    }
    
    finput.close();
    foutput.close();
    return 0;
}

