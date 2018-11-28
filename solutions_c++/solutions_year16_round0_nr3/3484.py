
#include <cmath>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#define llu long long int
using namespace std;

llu ipow(llu base, llu exp) {
    llu result = 1llu;
    while(exp) {
        if(exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

void getNum(vector<llu>& num, string str) {
    for(llu i = 2; i < 11; i++) {
        llu val = 0;
        for(llu j = (llu)str.length() - 1, k = 0; j >= 0; j--, k++)
            val += (str[j] - '0')*ipow(i, k);
        num[i - 2] = val;
        if(val < 0) cout << "error";
    }
}

bool IsPrime(llu n){
    if(n <= 3) return n > 1;
    if(n % 2 == 0 || n % 3 == 0) return false;
    for(llu i = 5; i*i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

bool IsNotPrime(vector<llu> num) {
    for(llu i = 0; i < 9; i++) if(IsPrime(num[i]) == true) return false;
    return true;
}

void getDivisor(vector<llu>& divisor, vector<llu> num) {
    for(llu i = 0; i < 9; i++) {
        for(llu j = 2; ; j++) {
            if(num[i]%j == 0) {
                divisor[i] = j;
                break;
            }
        }
    }
}

string decToBin(llu num, llu len) {
    string str;
    while(num != 0) {
        llu i = num%2;
        str += to_string(i);
        num /= 2;
    }
    while(str.length() < len) str += '0';
    reverse(str.begin(), str.end());
    return str;
}

int main() {
    llu T, N, J;
    ifstream reader("input.txt");
    ofstream writer("output.txt");
    reader >> T;
    for(llu i = 0; i < T; i++) {
        reader >> N >> J;
        writer << "Case #" << i + 1 << ": \n";
        llu max = ipow(2, N) - 1;
        for(llu k = 0; k < J; ) {
            string str = decToBin(max, N);
            vector<llu> divisor(9, 0), num(9, 0);
            getNum(num, str);
            if(IsNotPrime(num)) {
                getDivisor(divisor, num);
                k++;
                writer << str << " ";
                for(llu m = 0; m < 9; m++) writer << divisor[m] << " ";
                writer << endl;
            }
            max -= 2;
        }
    }
    reader.close();
    writer.close();
    return 0;
}

















