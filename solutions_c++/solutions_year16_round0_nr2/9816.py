//
//  main.cpp
//  CodeJam16Pancakes
//
//  Created by Tanu on 4/9/16.
//  Copyright © 2016 Tanu Singhal. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{
    
    int T;
    cin>>T;

    string pancakeArrays[100];
    
    for(int i=0;i<T;i++)
    {
        cin>>pancakeArrays[i];
    }
    
    for(int i=0;i<T;i++)
    {
        int flips = 0;
        for(int c = 0; pancakeArrays[i][c]!=0;c++)
        {
            if(pancakeArrays[i][c] == '+')
                continue;
            
            if(c==0)
                flips++;
            else if(pancakeArrays[i][c-1] == '-')
                continue;
            else
                flips+=2;
        }
        cout<<"Case #"<<i+1<<": "<<flips<<endl;
    }
    
    return 0;
}
