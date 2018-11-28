//
//  main.cpp
//  Fair and Square
//
//  Created by Matthew Wein on 4/13/13.
//  Copyright (c) 2013 Matthew Wein. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>

#include "Palindrome.h"

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream file (argv[1]);
    
    if (file.is_open())
    {
        while (file.good())
        {
            string line;
            getline(file,line);
            if (line != "")
            {
                istringstream iss (line);
                
                int testcases;
                iss >> testcases;
                
                for (int i = 0; i < testcases; i++)
                {
                    cout << "Case #" << i + 1 << ": ";
                    
                    int A, B;
                    getline(file,line);
                    istringstream iss (line);
                    iss >> A >> B;
                    
                    int count = 0;
                    for (int i = A; i <= B; i++)
                    {
                        if (CFairAndSquare::IsPalindrome(i) &&
                            CFairAndSquare::IsFair(i))
                        {
                            count++;
                        }
                    }
                    
                    cout << count << endl;
                }
            }
        }
        
        file.close();
    }
    else
    {
        cout << "<Bad File>: " << argv[1] << endl;
    }
    
    return 0;
}