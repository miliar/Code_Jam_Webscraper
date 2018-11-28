#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int sq;

int notprime(long long n) {
    sq = ceil(sqrt(n));
    for(int i = 3; i <= sq; i += 2) {
        if(n % i == 0) return i;
    }
    return 0;
}
int temp;

string bin(int n) {
    string s;
    while(n) {
        s = (n & 1 ? "1" : "0") + s;
        n >>= 1;
    }
    return s;
}

int main() {
    freopen("C-small-attempt0.out", "w", stdout);
    int n = 32769;
    int found = 0;
    printf("Case #1:\n");
    while(found < 50) {
        string s = bin(n);
        if(!notprime(n)) {
            n += 2;
            continue;
        }
        vector<int> factors;
        for(int b = 2; b <= 10; b++) {
            if((temp = notprime(stoll(s, NULL, b)))) {
                factors.push_back(temp);
            } else {
                break;
            }
        }
        n += 2;
        if(factors.size() != 9) continue;
        printf("%s", s.c_str());
        for(int i = 0; i < 9; i++)
            printf(" %d", factors[i]);
        printf("\n");
        found++;
    }
    return 0;
}
