#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <cmath>
#define ll long long

std::string flip(std::string ck) {
    //std::string ck = cake.substr(0, cake.length());
    for (int i = 0; i < ck.length(); i++) {
        if (ck[i] == '-') {
            ck[i] = '+';
        }
        else {
            ck[i] = '-';
        }
    }
    return ck;
}


ll getResult(std::string cakes) {
    if (cakes.length() <= 0) {
        return 0;
    }
    else if (cakes[cakes.length() - 1] == '+') {
        return getResult(cakes.substr(0, cakes.length() - 1));
    }
    else {
        int i = 0;
        while ((i < cakes.length()) && (cakes[i] == '+')) {
            i++;
        }
        if (i > 0) {
            std::string next = cakes.substr(0, i);
            next = flip(next);
            next.append(cakes.substr(i, cakes.length() - i));
            return 1 + getResult(next);
        }
        else {
            i = 0;
            while ((i < cakes.length()) && (cakes[i] == '-')) {
                i++;
            }
            std::string next = cakes.substr(0, i);
            next = flip(next);
            if (i < cakes.length()) {
                next.append(cakes.substr(i, cakes.length() - i));
            }
            return 1 + getResult(next);
        }

    }
} 

int main() {
    ll nTests;
    std::cin >> nTests;
    std::string N;
    ll result;
    for (ll i = 1; i <= nTests; i++) {
        std::cin >> N;
        result = getResult(N);
        std::cout << "Case #" << i << ": " << result << std::endl;
    }
    return 0;
}