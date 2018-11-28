#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isPal(long long num) {
    int numDigits=0, digits[15];
    while(num > 0) {
        digits[numDigits++] = num%10;
        num/=10;
    }
    for(int n=0; n<numDigits/2; n++) {
        if(digits[n] != digits[numDigits - n - 1])
            return false;
    }
    return true;
}

long long makePal(int num, bool overlap) {
    int numDigits=0, digits[15];
    for(int n=num; n > 0; n/=10) {
        digits[numDigits++] = n%10;
    }
    long long res = num;
    for(int n=(overlap?1:0); n<numDigits; n++) {
        res *= 10;
        res += digits[n];
    }
    return res;
}

int main() {
    vector<long long> squares;
    for(int n=1; n<10000; n++)
        for(int b=0; b<2; b++) {
            long long pal = makePal(n, b);
            if(isPal(pal*pal))
                squares.push_back(pal*pal);
        }
    sort(squares.begin(), squares.end());
    int ncases;
    cin>>ncases;
    for(int caseNum=0; caseNum < ncases; caseNum++) {
        int lower, upper;
        cin>>lower>>upper;
        cout<<"Case #"<<caseNum+1<<": "<<(upper_bound(squares.begin(), squares.end(), upper) - lower_bound(squares.begin(), squares.end(), lower))<<"\n";
    }
}
