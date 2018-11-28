#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

void printJamCoin(vector<int> jamCoin) {
    for (int i = 0; i < jamCoin.size(); i++) {
        cout << jamCoin[i];
    }
}

int findRemainder(vector<int> number, int divisBy) {
    int modNum;
    if (divisBy > 10) {
        modNum = 100 % divisBy;
    } else {
        modNum = 10 % divisBy;
    }
    if (divisBy > 10) {
        while (number.size() >= 3) {
            int a = number[0];
            int b = number[1];
            int c = number[2];
            // remove first element
            number.erase(number.begin());
            int num = (a * modNum + b * 10 + c) % divisBy;
            if (num > 10) {
                number[0] = num / 10;
                number[1] = num % 10;
            } else {
                number.erase(number.begin());
                number[0] = num;
            }
        }
        if (number.size() == 1) {
            return number[0] % divisBy;
        } else {
            return (number[0] * 10 + number[1]) % divisBy;
        }
    } else {
        // take first 2 numbers;
        while (number.size() >= 2) {
            int a = number[0];
            int b = number[1];
            // remove first element
            number.erase(number.begin());
            number[0] = (a * modNum + b) % divisBy;
        }
        return number[0] % divisBy;
    }
    
}

bool isDivisible(vector<int> number, int divisBy) {
    return findRemainder(number, divisBy) == 0;
}

long long convertVecToNum(vector<int> number) {
    long long num = 0;
    int multiplyBy = 1;
    while (number.size() > 0) {
        num += number.back() * multiplyBy;
        multiplyBy *= 10;
        number.pop_back();
    }
    return num;
}

vector<int> convertNumToVec(long long result) {
    vector<int> number;
    while (result > 0) {
        number.push_back(result % 10);
        result /= 10;
    }
    std::reverse(number.begin(),number.end());
    return number;
}

vector<int> divideBy(vector<int> number, int diviser, int &remainder) {
    if (number.size() <= 8) {
        long long result = convertVecToNum(number);
        remainder = result % diviser;
        result /= diviser;
        return convertNumToVec(result);
    } else {
        int count = 0;
        vector <int> quotient;
        long temp = 0;
        for (int i = 0; i < number.size(); i++) {
            temp = temp*10 + number[i];
            if (temp < diviser) {
                quotient.push_back(0);
            } else {
                quotient.push_back(temp / diviser);
                temp = temp % diviser;
            }
        }
        while (quotient[0] == 0) {
            quotient.erase(quotient.begin());
        }
        remainder = temp;
        return quotient;
    }
}

vector<int> addVectors(vector<int> a, vector<int> b) {
    if (a.size() > b.size()) {
        int size = a.size() - b.size();
        for (int i = 0; i < size; i++) {
            b.insert(b.begin(), 0);
        }
    } else if (a.size() < b.size()) {
        int size = b.size() - a.size();
        for (int i = 0; i < size; i++) {
            a.insert(a.begin(), 0);
        }
    }
    
    vector<int> c(a.size() + 1);
    int carryOver = 0, sum = 0;
    for (int i = c.size() - 1; i > 0; i--) {
        int num3 = a[i-1] + b[i-1] + carryOver;
        carryOver = num3 / 10;
        sum = num3 % 10;
        c[i] = sum;
    }
    if (carryOver == 0) {
        c.erase(c.begin());
    } else {
        c[0] = carryOver;
    }
    return c;
}

vector<int> multiplyVectorByNum(vector<int> a, int num) {
    vector<int> orig = a;
    for (int i = 0; i < num-1; i++) {
        a = addVectors(a, orig);
    }
    
    return a;
}

vector<int> convertBaseXToBase10(vector<int> number, int x) {
    
    vector <int> result;
    result.push_back(0);
    for (int i = 0; i < number.size(); i++) {
        if (number[i] == 1) {
            vector<int> temp;
            if (i == number.size() - 1) {
                temp.push_back(1);
            } else {
                temp.push_back(1);
                for (int j = i + 1; j < number.size(); j++) {
                    temp = multiplyVectorByNum(temp, x);
                }
            }
            result = addVectors(result, temp);
        }
    }
    
    return result;
    
}

vector<int> convertJamCoinToBase(vector<int> jamCoin, int base) {
    jamCoin = convertBaseXToBase10(jamCoin, base);
    return jamCoin;
}

vector<int> generateJamCoin(vector<int> lastJamCoin) {
    vector<int> jamCoin = lastJamCoin;
    for (int i = jamCoin.size() - 2; i > 0; i--) {
        if (jamCoin[i] == 0) {
            jamCoin[i] = 1;
            for (int j = i + 1; j < jamCoin.size() - 1; j++) {
                jamCoin[j] = 0;
            }
            break;
        }
    }
    return jamCoin;
}

bool isJamCoin(vector<int> jamCoin) {
    vector<long> output;
    bool isJamCoin = true;
    for (int i = 2; i <= 10; i++) {
        vector<int> temp = convertJamCoinToBase(jamCoin, i);
        bool canDivide = false;
        for (int j = 2; j < 100; j++) {
            if (isDivisible(temp, j)) {
                canDivide = true;
                output.push_back(j);
                break;
            }
        }
        if (!canDivide) {
            isJamCoin = false;
            break;
        }
    }
    if (isJamCoin) {
        printJamCoin(jamCoin);
        cout << " ";
        for (int i = 0; i < output.size(); i++) {
            if (i != output.size() - 1) {
                cout << output[i] << " ";
            } else {
                cout << output[i] << endl;
            }
        }
    }
    return isJamCoin;
}

int main () {
    int numCases = 0;
    int N = 32;
    int j = 500;
    vector<int> jamCoin;
    jamCoin.push_back(1);
    for (int i = 0; i < N - 2; i++) {
        jamCoin.push_back(0);
    }
    jamCoin.push_back(1);
    
    cout << "Case #1:" << endl;
    int foundJamCoins = 0;
    while (foundJamCoins < j) {
        if (isJamCoin(jamCoin)) {
            foundJamCoins++;
        }
        bool shouldFinish = true;
        for (int i = 0; i < jamCoin.size(); i++) {
            if (jamCoin[i] != 1) {
                shouldFinish = false;
                break;
            }
        }
        if (shouldFinish) {
            break;
        }
        jamCoin = generateJamCoin(jamCoin);
    }
    
    /*
    for (int i = 0; i < 7; i++) {
        jamCoin = generateJamCoin(jamCoin);
        printJamCoin(jamCoin);
    } */

}
