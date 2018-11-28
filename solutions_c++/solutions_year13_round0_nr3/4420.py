#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int is_palindrome(unsigned long long v) {
    unsigned long long orig = v;
    unsigned long long u = 0;
    while(v != 0) {
        u *= 10;
        u += v%10;
        v /= 10;
    }
    return u == orig;
}

int countfs(unsigned long long A, unsigned long long B) {
    unsigned long long start = (unsigned long long)floor(sqrt((double)A));
    unsigned long long end = (unsigned long long)ceil(sqrt((double)B));
    int count = 0;
    for (unsigned long long a = start; a<=end; a++) {
        if (is_palindrome(a) && is_palindrome(a*a)) {
            if (a*a < A || a*a > B)
                continue;
            count++;
        }
    }
    return count;
}

int main(int argc, char *argv[])
{
    int count;
    ifstream fin("C-small-attempt0.in");
    ofstream fout("output");
    fin >> count;
    for (int c = 0; c < count; c++) {
        unsigned long long A,B;
        fin >> A >> B;
        fout << "Case #" << c + 1 <<": "<<  countfs(A,B) << endl;
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
