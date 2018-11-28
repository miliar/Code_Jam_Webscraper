#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

uint64_t constParts[9];
int cccount = 0;
ofstream outfile("C-large.out");

bool is_prime(uint64_t num){
    if(num <= 3){
        return num > 1;
    }
    else if(num % 2 == 0 || num % 3 == 0){
        return false;
    }
    else{
        for (uint64_t i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

uint64_t diviser(uint64_t num){
    if(num % 2 == 0){
        return 2;
    }
    else if(num % 3 == 0){
        return 3;
    }
    else{
        for (uint64_t i = 5; i * i <= num; i += 6) {
            if (num % i == 0) {
                return i;
            }
            else if(num % (i + 2) == 0){
                return i+2;
            }
        }
    }
}

uint64_t u_pow(uint64_t base, int exp){
    uint64_t result = base;
    for (int i = 1; i < exp; i++)
    {
        result = result * base;
    }
    return result;
}

void generateNum(string number, int strLen){
    if(strLen == 14){
        if(cccount >= 500){
            return;
        }
        bool isJamcoin = true;
        uint64_t divisers[9];
        for (uint64_t i = 2; i < 11; ++i)
        {
                // cout<< "keke" << endl;
            uint64_t convNum = constParts[i-2];
            for (int j = 0; j < 14; j++)
            {
                if(number[j] == '1'){
                    convNum += u_pow(i,14-j);
                    // cout << convNum << endl;
                }

            }


            if (is_prime(convNum))
            {
                isJamcoin = false;
                break;
            }
            else{
                divisers[i-2] = diviser(convNum);
            }
        }

        if(isJamcoin && cccount < 500){
            number = "1" + number + "1";
            outfile << number << number;
            for (int i = 0; i < 9; ++i)
            {
                outfile << " " << divisers[i];
            }
            outfile << endl;
            cccount++;
        }

    }
    else{
        generateNum(number + "0",strLen+1);
        generateNum(number + "1",strLen+1);
    }
}

int main(){
    ifstream infile("C-large.in");

    int length,n,j;
    infile >> length;
    infile >> n;
    infile >> j;

    for (uint64_t i = 0; i < 9; ++i)
    {
        constParts[i] = u_pow(i+2,n/2-1) + 1;
    }

    outfile << "Case #1:" << endl;
    generateNum("",0);

    return 0;
}
