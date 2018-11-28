//
//  main.cpp
//  code_jam_qualification_round
//
//  Created by hijackyan on 4/11/15.
//  Copyright (c) 2015 hackerrank. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
int main() {
    int T;
    cin>>T;
    int case_number = 1;
    while(T--)
    {
        int result = 0;
        int level, num, acc = 0;
        string t;
        cin>>level;
        cin>> t;
        for(int i = 0; i <= level; i++)
        {
            num = t[i] - '0';
            if(num != 0 && acc < i)
            {
                result += i-acc;
                acc = i;
            }
            acc += num;
        }
        cout<<"Case #"<<case_number++<<": "<<result<<endl;
    }
}
