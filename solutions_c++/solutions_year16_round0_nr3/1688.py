#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <math.h>
#include <stdlib.h>

using namespace std;

string firstPart;

long long power(int a, int n) {
    long long result = 1;
    for (int i=0;i<n;i++) {
        result *= a;
    }
    return result;
}

long long convertToBase10(string num, int fromBase) {
    long long result = 0;
    int numLength = num.length();
    for (int i=0;i<numLength;i++) {
        result += (num[i] - '0') * power(fromBase,numLength-1-i);
    }
    return result;
}

long long convertToBase10Last16Digits(string num, int fromBase) {
    long long result = 0;
    int numLength = num.length();
    for (int i=16;i<numLength;i++) {
        result += (num[i] - '0') * power(fromBase,numLength-1-i);
    }
    return result;
}

int maybePrime(long long value, int base) {
    // Don't need to know precisely that value is a prime, we quickly find out if it is not a prime
    for (int i=2;i<100;i++) {
        long long value1 = power(base,15)%i;//value of first 16 character 100000000000000...
        value1 *= power(base,16);
        if ((value1+value)%i == 0) {
            return i;
        }
    }
    return -1;
}

bool checkJamCoin(string jamCoin, int nontrivialDivisor[9]) {
    for (int i=2;i<=10;i++) {
        long long value = convertToBase10Last16Digits(jamCoin, i);
        int divisor = maybePrime(value, i);
        if (divisor == -1) {
            return false;
        } else {
            nontrivialDivisor[i-2] = divisor;
        }
    }
    return true;
}

void generateJamCoin(int N, int level, string strGenerated, int &countSolution, int J) {
    if (countSolution == J) {
        return;
    }
    if (level == N) {
        int nontrivialDivisor[9];
        // For 32 digits jam coin, there are numerous of solutions, so, we just need to generate the last 16 digits, the first 16 digits just keep it as below.
        if (checkJamCoin(firstPart + '1' + strGenerated + '1', nontrivialDivisor)) {
            countSolution++;
            cout<<firstPart + '1' + strGenerated + '1';
            for (int i=2;i<=10;i++) {
                cout<<" "<<nontrivialDivisor[i-2];
            }
            cout<<endl;
        }
    } else {
        generateJamCoin(N, level+1, strGenerated+'0', countSolution, J);
        generateJamCoin(N, level+1, strGenerated+'1', countSolution, J);
    }
}

int main() {
    ifstream fin ("/Users/LeonardNguyen/Documents/projects/ios/usaco/sample.in");
    
    int T, N, J;
    fin>>T>>N>>J;
    
    if (N== 32) {
        firstPart = "1000000000000000";
        N = 16;
    } else {
        firstPart = "";
    }
    
    int countSolution = 0;
    cout<<"Case #1: "<<endl;
    generateJamCoin(N-2, 0, "", countSolution, J);
    return 0;
}

