#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <string>
using namespace std;


template<typename T>
string to_string(const T& t) {
    ostringstream os;
    os << t;
    return os.str();
}

string toBinary(long long n) {
    std::string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return r;
}

long long toDecimal(long long n, long long f) {
    long long factor = 1;
    long long total = 0;

    while (n != 0) {
        total += (n%10) * factor;
        n /= 10;
        factor *= f;
    }

    return total;
}

bool isPrime(long long number){
    if (number < 2) return false;
    if (number == 2) return true;
    if (number % 2 == 0) return false;
    for (long long i=3; (i*i)<=number; i+=2) {
        if (number % i == 0 ) return false;
    }
    return true;
}

long long getfactor(long long number, long long base) {
    for (long long i=3; i <= number/2; i++) {
        if (number % i == 0) {
            return i;
        }
    }
}

int main() {
    // Initialization and Input
    ifstream inFile;

    inFile.open("C:\\Users\\Junaid\\Desktop\\CodeBlocks\\cjin.txt");

    long long q, n, j, count, mindecimal, minbinary, temp, flag;
    vector<long long> jamcoins;

	inFile >> q;
    inFile >> n;
    inFile >> j;
    string maxstr = ""; string minstr = ""; string tempstr;
    count = 0; flag = 1;
    long long counter =0;
    for (long long i = 0; i < n; i++) {
        minstr = minstr + '0';
    }

    minstr[0] = '1'; minstr[n-1] = '1';
    mindecimal = toDecimal(atoll(minstr.c_str()), 2);

    while (1) {
        flag = 1;
        tempstr = toBinary(mindecimal);
        if (tempstr[0] == '1' && tempstr[n-1] == '1') {
            minbinary = atoll(tempstr.c_str());
            for (long long i = 2; i < 11; ++i) {
                temp = toDecimal(minbinary, i);
                if (isPrime(temp) == true) {
                    flag = 0;
                    break;
                }
            }

            if (flag == 1) {
                jamcoins.push_back(minbinary);
                count++;
                if (count == j) {
                    break;
                }
            }
        }
        mindecimal++; counter++;
    }

    cout << "Case #1:" << endl;

    for (long long i = 0; i < j; i++) {
        cout << jamcoins[i] << " ";

        for (long long j = 2; j < 11; j++) {
            temp = toDecimal(jamcoins[i], j);
            cout << getfactor(temp, j) << " ";
        }
        cout << endl;
    }


    return 0;
}
