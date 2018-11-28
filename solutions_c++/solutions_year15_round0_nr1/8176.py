//
//  main.cpp
//  C++ test
//
//  Created by HIUKIN on 15/4/11.
//  Copyright (c) 2015年 HIUKIN. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <fstream>

#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
    
    string filepath = "/Users/hiukin/Downloads/A-large.in";
    ifstream file(filepath);
    string filepath2 = "/Users/hiukin/Downloads/A-large.out";
    ofstream outfile(filepath2);
    
    if(file.is_open())
    {
        int cases;
        file >> cases;
        
        for(int index = 1; index <= cases; index++)
        {
            outfile << "Case #" << index << ": ";
            
            int num;
            file >> num;
            file.get();             //ignore ' '
            
            int counter = 0;
            int curS = 0;
            
            for(int i = 0; i < num+1; i++)
            {
                char c;
                int s;
                
                file.get(c);
                s = c - '0';
                
                curS += s;
                
                if( curS <= i )
                {
                    curS++;
                    counter++;
                }
                
            }
            
            outfile << counter << endl;
        }
        
    }
    else
    {
        cout << "cannot open" << endl;
    }
    
    file.close();
    outfile.close();
    
    return 0;
}
