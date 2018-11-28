#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <cmath>
#define ll long long

bool digits[10];

void initDigits() {
    for (int i = 0; i < 10; i++) {
        digits[i] = false;
    }
}

bool allTrue() {
    for (int i = 0; i < 10; i++) {
        if (!digits[i]) {
            return false;
        }
    }
    return true;
}

ll getResult(ll n) {
    if (n == 0) {
        return -1;
    }
    ll x = 0;
    while (!allTrue()) {
        x += n;
        std::string number = std::to_string(x);
        for (int i = 0; i < number.length(); i++){
            digits[(int)(number[i]) - 48] = true;
        }
    }
    return x;
} 

int main() {
    ll nTests;
    scanf("%lld", &nTests);
    ll N;
    ll result;
    for (ll i = 1; i <= nTests; i++) {
        scanf("%lld", &N);
        initDigits();
        result = getResult(N);
        if (result < 0) {
            printf("Case #%lld: INSOMNIA\n", i);
        }
        else {
            printf("Case #%lld: %lld\n", i, result);
        }
    }
    return 0;
}