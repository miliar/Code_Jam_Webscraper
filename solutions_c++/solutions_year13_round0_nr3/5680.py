//
//  main.cpp
//  Google Code Jam
//
//  Created by Zhuo Li on 4/12/13.
//  Copyright (c) 2013 Zhuo Li. All rights reserved.
//
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool palindromeCheck(int num);
bool squareCheck(int num);

int main () {
    int input_size, temp, A, B;
    stringstream ss;
    ifstream myfile("C-small-attempt0.in");
    string first_line;
    getline(myfile, first_line);
    ss << first_line;
    ss >> input_size;
    temp = input_size;
    int *input = new int[input_size];
    int case_num = 0;
    int num_fair_square;
    while (temp!=0) {
        num_fair_square = 0;
        myfile>>A>>B;
        for (int i = A; i <= B; i++) {
            if(palindromeCheck(i)&&squareCheck(i)) {
                if (palindromeCheck((int)sqrt(i))) {
                    num_fair_square++;
                }
         }
        }
        input[case_num] = num_fair_square;
        case_num++;
        temp--;
    }
    int num = 1;
    while (input_size!=0) {
        cout<<"Case #"<<num<<": "<<input[num-1]<<"\n";
        num++;
        input_size--;
    }
    delete [] input;
    return 0;
}

bool palindromeCheck(int num)
{
    int digit;
    int rev = 0;
    int temp = num;
    while (num > 0)
    {
        digit = num % 10;
        rev = rev * 10 + digit;
        num = num / 10;
    }
    if (temp == rev) return true;
    return false;
}

bool squareCheck(int num)
{
    if (num < 0) return false;
    int a = (int) sqrt((double)num);
    if (a * a == num || (a+1) * (a+1) == num) return true;
    return false;
}

