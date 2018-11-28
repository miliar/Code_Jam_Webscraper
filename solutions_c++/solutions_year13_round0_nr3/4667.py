//
//  main.cpp
//  googlecode3
//
//  Created by Melody Pang on 14/04/2013.
//  Copyright (c) 2013 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    return n == root * root;
}

bool isPalindrome(int number) {
    int reverse = 0, copy = number;
    while(copy != 0) {
        reverse = reverse*10 + copy%10;
        copy /= 10;
    }
    return number == reverse;
}

int main(){
    ifstream infile("/Users/mellypang/Developer/googlecode/googlecode3/googlecode3/input.txt");
    
    if (!infile) {
        cout << "There was a problem opening file "
        << " for reading."
        << endl;
        return 0;
    }
    int nTests;
    infile >> nTests;
    ofstream myfile;
    myfile.open ("/Users/mellypang/Developer/googlecode/googlecode3/googlecode3/output.txt");
    for (int k = 0; k < nTests; ++k) 
    {
        int num,r,sum,temp;
        int min,max;
        vector<int> candidates;    
        vector<int> results;

        infile >> min;
        infile >> max;
    
        for(num=min;num<=max;num++)
        {
            if(isPalindrome(num) && is_perfect_square(num))
                candidates.push_back(num);
        }
        
        for(int i = 0;i<candidates.size();i++)
        {
            temp = sqrt(candidates[i]);
            if(isPalindrome(temp) || num < 10)
            {
                results.push_back(candidates[i]);
            }
        }
        
        myfile << "Case #" << k + 1 << ": " << results.size() << endl;        
    }
}

