#include <iostream>
#include <fstream>
#include <math.h>

#define MAX 100000000000000
#define DIGITS 15

using namespace std;

unsigned int t;
unsigned long long a;
unsigned long long b;
bool palindrome[MAX];

int is_palindrome(unsigned long long n) {
    if(palindrome[n]) {
        return 1;
    }

    char number[DIGITS];
    unsigned int l = sprintf(number, "%d", n);

    //cout << l << endl;
    //cout << number << endl;

    bool is_p = 1;
    for(unsigned int i=0; i<l/2 && is_p; i++) {
        if(number[i] != number [l-i-1]) {
           is_p = 0; 
        }
    }

    if(is_p) {
        palindrome[n] = 1;
    }

    return is_p;
}

int main(int argc, char *argv[]) {
    ifstream fin (argv[1]);
    ofstream fout (argv[2]);

    fin >> t;

    for(unsigned int i=0; i<t; i++) {
        //cout << "NEW CASE " << i << endl; 
        int fair_square = 0; 

        fin >> a >> b;

        if(a == 1) {
            fair_square += 1;
        }

        if(a < 4) {
            a = 4; // The first fair and square number after 1
        }

        for(unsigned long long j=a; j<=b; j++) {
            //cout << j << endl;
            unsigned int fair = is_palindrome(j);
            unsigned int fair_sqrt = 0;

            if(fair == 1) {
                unsigned long long sqrt_j = sqrt(j);
                if(sqrt_j * sqrt_j == j) {
                    fair_sqrt = is_palindrome(sqrt_j);
                }
            }

            if(fair && fair_sqrt) {
                fair_square += 1;
                //cout << "fair and square: " << j << " " << sqrt_j << endl;
            }
        }

        fout << "Case #" << i+1 << ": " << fair_square << endl;
    }

    return 0;
}
