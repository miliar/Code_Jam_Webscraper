#include <cstdio>
#include <string>
#include <bitset>
#include <iostream>
#include <cmath>
using namespace std;

bitset<16> incrementBitSetNum(const bitset<16>& curNum) {
    std::bitset<16> const b("1");
    std::bitset<16> const m("1");
    std::bitset<16> result;
    for (auto i = 0; i < result.size(); ++i) {
        std::bitset<16> const diff(((curNum >> i)&m).to_ullong() + ((b >> i)&m).to_ullong() + (result >> i).to_ullong());
        result ^= (diff ^ (result >> i)) << i;
    }
    
    return result;
}

long long isNumPrime(long long num)
{
    if(num <= 1)
        return -1;
    else if(num == 2)         
        return 2;
    else if(num % 2 == 0)
        return 2;
    else
    {
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) + 1);
        
        while(divisor <= upperLimit)
        {
            if(num % divisor == 0) {
                return divisor;
            }
            divisor += 2;
        }
        return -1;
    }
}

int main(){
    int noOfTestCases = 0, N = 0, J = 0, noOfOutputNums = 0, curBase = 10, curDivisor = -1;
    long long curBNum = 0, curNumL;
    bool isAllNonPrime = true;
    string curNumStr = "1", curStrOut = "";
    cin >> noOfTestCases >> N >> J;

    for(int curCase = 1; curCase <= noOfTestCases; curCase++) {
        for(int i = 1; i < N; i++) {
            curNumStr += "0";
        }

        bitset<16> curNum(curNumStr);
        cout << "Case #" << curCase << ":" << endl;
        while(noOfOutputNums <= J) {
            if(curNum[15] == 1 && curNum[0] == 1) {
                curBase = 1;
                isAllNonPrime = true;
                curStrOut = curNum.to_string();

                while(++curBase <= 10 && isAllNonPrime) {
                    curBNum = stol(curNum.to_string(), nullptr, curBase);
                    curDivisor = isNumPrime(curBNum);
                    if(curDivisor == -1) {
                        isAllNonPrime = false;
                        break;
                    }
                    curStrOut += " " + to_string(curDivisor);   
                }

                if(isAllNonPrime) {
                    cout << curStrOut << endl;
                    noOfOutputNums++;
                }
            }
            curNum = incrementBitSetNum(curNum);
        }

    }
    
    return 0;
}
