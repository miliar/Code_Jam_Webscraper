//
//  main.cpp
//  CodeJamQualPr1
//
//  Created by Oleksandr Loyko on 4/8/16.
//  Copyright © 2016 Oleksandr Loyko. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string to_dream(string num);

int main(int argc, const char * argv[]) {
    
    ifstream input("input.in");
    int case_n;
    input >> case_n;
    string num;
    getline(input,num);
    ofstream output;
    output.open("output.out");
  
    for(int i = 1; i <= case_n; i++)
    {
        getline(input, num);
        output << "Case #" << i << ": " << to_dream(num) << endl;
        
    }
    
    
    
    input.close();
    output.close();
    return 0;
}
string to_dream(string num)
{
    if(stoi(num)==0) return "INSOMNIA";
    string number = num;
  string test = "0123456789";
    int mult = 2;
    while(true)
    {
        for(int i = 0; i < number.length(); i++)
        {
            for(int j = 0; j < test.length(); j++)
            {
                if(number.find(test[j]) != string::npos)
                    test.erase(j,1);
                if(test.empty())
                    return number;
            }
        }
        number = to_string(stoi(num)*mult);
        mult++;
    
    }
}

