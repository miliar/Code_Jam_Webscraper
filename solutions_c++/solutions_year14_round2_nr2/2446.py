//
//  main.cpp
//  New_Lottery_Game
//
//  Created by CuiLei on 5/4/14.
//  Copyright (c) 2014 wolfshow. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    //std::cout << "Hello, World!\n";
    int T;
    
    int A,B,K;
    
    cin >> T;
    
    int count;
    
    for(int cc = 1; cc <=T; cc++)
    {
        cin >> A >> B >> K;
        count = 0;
        for(int i = 0; i < A; i++)
        {
            for(int j = 0; j < B; j++)
            {
                for(int k = 0; k < K; k++)
                {
                    if((i & j) == k)
                        count++;
                }
            }
        }
        
        cout << "Case #" << cc << ": " << count << endl;
    }
    
    return 0;
}

