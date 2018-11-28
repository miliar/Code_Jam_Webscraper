//
//  main.cpp
//  codeJam
//
//  Created by Zurab Kachukhashvili on 4/13/13.
//  Copyright (c) 2013 Zurab Kachukhashvili. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool isPalindrom(int k)
{
    string check = to_string(k);
    long length = check.length();
    for (int i = 0; i < length / 2 ; i++) {
        if (check[i] != check[length-1-i]) {
            return false;
        }
    }
    return true;
}

bool isFairPalindrom(int k)
{
    bool sqrPalindrom(false);
    double t = sqrt(k);

    if (t == (int) t) {
        sqrPalindrom = isPalindrom((int)t);
    }
    if (isPalindrom(k) &&  sqrPalindrom) {
        return true;
    }
    return false;
}

int main()
{
    int k;
    ifstream ifs("input.txt");
    ofstream ofs("output.txt");
    ifs>>k;
    for (int p = 0; p < k; p++)
    {
        int count(0);
        int start,end;
        ifs>>start>>end;
        
        for (int s = start; s <= end; s++) {
            if (isFairPalindrom(s)) {
                count++;
            }
        }
        ofs<<"Case #"<<p+1<<": "<<count<<endl;
    }
    
    
    return 0;
}

