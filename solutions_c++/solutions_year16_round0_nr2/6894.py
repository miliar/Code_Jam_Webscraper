//
//  main.cpp
//  CodeJamPr2
//
//  Created by Oleksandr Loyko on 4/9/16.
//  Copyright © 2016 Oleksandr Loyko. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <fstream>
using namespace std;

int min_num(string stck);
int main(int argc, const char * argv[]) {
    
    ifstream input("input.in");
    ofstream output;
    output.open("output.out");
    int case_n;
    input >> case_n;
    string pan_stack;
    getline(input, pan_stack);
    
    for(int i = 1; i <= case_n; i++)
    {
        getline(input,pan_stack);
        output << "Case #" << i << ": " << min_num(pan_stack) << endl;
        
        
    }
    
    input.close();
    output.close();
    return 0;
}
int min_num(string stck)
{
    int count = 0;
    vector<char> pancake;
    for(int i = 0; i < stck.length();i++)
    {
        pancake.push_back(stck[i]);
    }
   
    for(int i = 1; i < pancake.size();i++)
    {
        if(pancake.size()>=2)
        {
            
            if(pancake[i] != pancake[i-1])
            {
                for(int j = 0; j < i; j++)
                {
                    if(pancake[j]=='+')
                        pancake[j] = '-';
                    else
                        pancake[j] = '+';
                }
                count++;
                i = 0;
            }
            
        }
    }
    
        if (pancake[0] == '-')
        {
            count++;
            return count;
        }
        else
            return count;

}