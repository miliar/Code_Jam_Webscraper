#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    //odd bases: even number 1's
    //1 mod 3 bases: 0 mod 3 number 1's
    //2 mod 3 bases: equal number in odd and even slots
    //6, 12, etc. number of 1's
    freopen("./large.out", "w", stdout);
    string divisors = " 3 2 3 2 7 2 3 2 3\n";

    cout << "Case #1:\n";
    int counter = 0;
    for (int a=0; a<14; ++a) {
        for (int b=a+1; b<15; ++b) {
            for (int c=0; c<14; ++c) {
                for (int d=c+1; d<15; ++d) {
                    char odds[15], evens[15];
                    for (int index=0; index<15; ++index) {
                        odds[index] = '0';
                        evens[index] = '0';
                        if (index == a || index == b) {
                            odds[index] = '1';
                        }
                        if (index == c || index == d) {
                            evens[index] = '1';
                        }
                    }
                    cout << '1';
                    for (int index=0; index<15; ++index) {
                        cout << odds[index] << evens[index];
                    }
                    cout << '1';
                    cout << divisors;
                    ++counter;
                    if(counter>=500) {
                        return 0;
                    }
                }
            }
        }
    }
    return 0;
}
