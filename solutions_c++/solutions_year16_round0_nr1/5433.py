//
//  main.cpp
//  Test
//
//  Created by Abhiraj Khare on 4/9/16.
//  Copyright © 2016 Abhiraj Khare. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

int checkDigit(long long int digit, int code);

int main() {
    int T;
    long long int N;
    cin>>T;
    for(int i=0; i<T; i++)
    {
        cin>>N;
        
        int bitCode = 0;
        int mult = 0;
        while(N != 0 && bitCode!=1023)
        {
            mult++;
            bitCode = checkDigit(mult*N, bitCode);
        }
        if(N == 0)
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<mult*N<<endl;
    }
    return 0;
}

int checkDigit(long long int digit, int code)
{
    while(digit!=0)
    {
        int bit = pow(2, digit%10);
        code |=  bit;
        digit /= 10;
    }
    return code;
}
