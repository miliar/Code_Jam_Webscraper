//
//  main.cpp
//  Google Code Jam 2015
//
//  Created by Praveen Kulkarni on 11/04/15.
//  Copyright (c) 2015 Praveen. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
int main(int argc, const char * argv[]) {
    unsigned long T, S, fr, count;
    int num;
    string str;
    cin >> T;
    for (int N=1; N<=T; ++N)
    {
        count = fr = 0;
        cin >> S >> str;
        for (int i=0; str[i]; ++i)
        {
            num = str[i] - '0';
            if (i>count)
            {
                fr += i - count;
                count = i;
            }
            count += num;
        }
        cout << "Case #" << N << ": " << fr << endl;
    }
    return 0;
}
