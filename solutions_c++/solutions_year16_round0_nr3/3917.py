//
//  JamCoin.cpp
//  Coin Jam
//
//  Created by Corey Woodfield on 4/8/16.
//  Copyright © 2016 Corey Woodfield. All rights reserved.
//

#include "JamCoin.hpp"

JamCoin::JamCoin(int size) : size(size) {
    jamCoin = "1";
    for (int i = 1; i < size - 1; ++i) {
        jamCoin += "0";
    }
    jamCoin += "1";
};

JamCoin::JamCoin(string jamCoin) : jamCoin(jamCoin), size(jamCoin.length()) {}

unsigned long long JamCoin::baseX(int x) {
    cout << "base" << x;
    unsigned long long result = 0;
    for (int i = 0; i < size; ++i) {
        cout << "y ";
        if (atoi(jamCoin.substr(i,1).c_str()) == 1) {
            result += pow(x, ((size - 1) - i));
        }
    }
    cout << endl;
    return result;
}

string JamCoin::findDivisors() {
    cout << "findDivisors" << endl;
    stringstream ss;
    vector<unsigned long long> divisors;
    for (int i = 2; i <= 10; ++i) {
        unsigned long long baseI = baseX(i);
        bool notPrime = false;
//        baseI = baseI % 1000000007;
        if (baseI == 0) {
            divisors.push_back(1000000007);
            ss << " " << 2;
            notPrime = true;
        } else if ((baseI % 2) == 0) {
            divisors.push_back(2);
            ss << " " << 2;
            notPrime = true;
        } else {
            for (unsigned long long j = 3; j < sqrt(baseI); j += 2) {
                if ((baseI % j) == 0) {
                    divisors.push_back(j);
                    ss << " " << j;
                    notPrime = true;
                    break;
                }
            }
        }
        if (!notPrime) {
            cout << "notPrime" << endl;
            return "";
        }
    }
    cout << endl;
    return ss.str();
}

bool JamCoin::addTwo() {
    cout << "addTwo" << endl;
    for (int i = size - 2; i >= 0; --i) {
        if (jamCoin[i] == '0') {
            jamCoin[i] = '1';
            return true;
        } else if (i == 0) {
            break;
        } else {
            jamCoin[i] = '0';
        }
    }
    return false;
}

string JamCoin::findJamCoin() {
    cout << "findJamCoin" << endl;
    stringstream ss;
    string divisors("");
    string jc;
    while (divisors == "") {
        jc = jamCoin;
        cout << jc << " ";
        divisors = findDivisors();
        if(!addTwo()) {
            cout << "broke" << endl;
        }
    }
    ss << jc << divisors;
    return ss.str();
}

void JamCoin::findJamCoins(int x, ofstream& out) {
    out << "Case #1:" << endl;
    vector<string> jamCoins;
    while (jamCoins.size() < x) {
        jamCoins.push_back(findJamCoin());
        out << jamCoins[jamCoins.size() - 1] << endl;
    }
}

int JamCoin::getSize() {
    return size;
}

string JamCoin::getJamCoin() {
    return jamCoin;
}












