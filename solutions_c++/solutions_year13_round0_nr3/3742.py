#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream> 
#include <string>

using namespace std;

typedef int number;

string toString(number n) {
    ostringstream ss;
    ss << n;
    return ss.str();
}

bool isPalindrome(number n) {
    string str = toString(n);
    int length = str.length();

    for(int i = 0; i < length / 2; i++) {
        if(str[i] != str[length - 1]) return false;
    }

    return true;
}

void solveCase() {
    //read bounds
    number a, b;
    cin >> a >> b;

    a = ceil(sqrt(a));
    b = number(sqrt(b));

    int n = 0;
    for(number i = a; i <= b; i++) {
        if(isPalindrome(i) && isPalindrome(i * i)) n++;
    }

    //output result
    cout << n << endl;
}

int main() {
    int caseCount;
    cin >> caseCount;

    for(int i = 1; i <= caseCount; i++) {
        printf("Case #%d: ", i);
        solveCase();
    }

    return 0;
}
