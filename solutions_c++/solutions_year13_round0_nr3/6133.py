#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <cstdlib>
#include <math.h>

using namespace std;
int main() {
    int testcases = 0;
    char filename[] = "C-small.in";
    std::ifstream fileRead;
    fileRead.open(filename, ios::in);
    if(!fileRead.is_open()) {
        std::cout <<"Failed to open file:" << filename << std::endl;
        return 0;
    }
    char line[1000];
    memset(line, '\0', 1000);
    fileRead.getline(line, 1000);
    testcases = atoi(line);
    for(int test=0; test < testcases; ++test) {
        int num1 = 0, num2 = 0;
        fileRead >> num1 >> num2;
        int output = 0;
        fileRead.getline(line, 1000);
        //std::cout <<" num1: " << num1 <<", num2:" << num2 << std::endl;
        for(int i = num1; i <= num2; ++i) {
            int sqrt1 = sqrt(i);
            if( sqrt1 * sqrt1 == i) {
                
                int digits = 0;
                int dd = sqrt1;
                while(dd) {
                    digits++;
                    dd /= 10;
                }
                //std::cout << "digits:" << digits << std::endl;
                bool flag = true;
                for(int ll =1; ll < digits; ++ll) {
                    int exp1 = pow(10, digits -ll);
                    int exp2 = pow(10, ll);
                    int exp3 = exp2/10;
                    if((sqrt1 / exp1)% 10 != (sqrt1 % exp2) / exp3) {
                       // std::cout <<"p1:" << sqrt1;
                        flag = false;
                        break;
                    }
                }
                if(flag) {
                    int digits = 0;
                    int dd = i;
                    while(dd) {
                        dd /= 10;
                        digits++;
                    }
                    //std::cout << "digits:" << digits << std::endl;
                    for(int ll =1; ll < digits; ++ll) {
                        int exp1 = pow(10, digits -ll);
                        int exp2 = pow(10, ll);
                        int exp3 = exp2 / 10;
                        if( (i / exp1) %10 != (i % exp2)/ exp3) {
                      //      std::cout <<"p1:" << (i / exp1) %10 <<", p2:" << i / exp2 << std::endl;
                            flag = false;
                            break;
                        }
                    }
                }
                if(flag) {
                    output++;
                }
            }
        }
        std::cout <<"Case #" << test+1 <<": " << output << std::endl;
    }
    return 0;
}

