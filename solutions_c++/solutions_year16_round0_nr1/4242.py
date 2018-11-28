#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <vector>
#include <set>
#include <string>

typedef long long int lli;

using namespace std;

lli n;
bool digits[10];

bool checkDigits(){
    for (int i = 0; i < 10; i++){
        if (digits[i] == false){
            return false;
        }
    }
    return true;
}

bool addDigits(lli number){
    if (number == 0){
        digits[0] = true;
        return checkDigits();
    }
    while (number != 0){
        digits[number % 10] = true;
        number /= 10;
    }
    return checkDigits();
}

void testIt(const int testNUM){
    for (int i = 0; i < 10; i++){
        digits[i] = false;
    }
    scanf("%d", &n);
    if (n == 0){
        printf("case #%d: INSOMNIA\n", testNUM);
        return;
    }
    addDigits(n);
    lli buffer = n;
    while (true){
        if (checkDigits()){
            break;
        }
        buffer += n;
        addDigits(buffer);
    }
    printf("case #%d: %d\n", testNUM, buffer);
}

int main(){
    freopen("A_small.out", "w+", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        testIt(i + 1);
    }
    return 0;
}

