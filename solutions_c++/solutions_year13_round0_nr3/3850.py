#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

/* function to determine if a number is palindrome */
static bool isPalindrome(unsigned long long int x)
{
    unsigned long long int div = 1;
    while (x / div >= 10) {
        div *= 10;
    }       

    while (x != 0) {
        unsigned long long int l = x / div;
        unsigned long long int r = x % 10;
        if (l != r) return false;
        x = (x % div) / 10;
        div /= 100;
    }

    return true;
}

/* main program logic */
int main(int argc, char* argv[])
{
    if(argc < 2) {
        cout << "No input file provided" << endl;
        return 1;
    }

    /* open files */
    ifstream fin(argv[1], ifstream::in);
    ofstream fout("out.txt", ofstream::out);

    /* get testcase count */
    int T = 0;
    fin >> T;

    /* process testcases */
    for(int t=0; t < T; t++) {
        unsigned long long int lower;
        unsigned long long int upper;
        unsigned long long int sqRoot;
        unsigned long long int fairSqaureCnt = 0;
        

        fin >> lower;
        fin >> upper;

        sqRoot = (unsigned long long int)sqrt(upper);

        /* search numbers till limit */
        for(unsigned long long int i = 1; i <= sqRoot; i++) {
            unsigned long long int square = i*i;
            if(square >= lower && isPalindrome(i) && isPalindrome(square)) {
                fairSqaureCnt++;
            }
        }
        cout << "Case #" << t+1 << ": " << fairSqaureCnt << endl;
        fout << "Case #" << t+1 << ": " << fairSqaureCnt << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
