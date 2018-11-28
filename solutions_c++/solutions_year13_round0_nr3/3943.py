#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

static bool isPalindrome(unsigned long long int x)
{
    unsigned long long int div = 1;
    while (x / div >= 10) {
        div *= 10;
    }       

    while (x != 0) {
        unsigned long long int low = x / div;
        unsigned long long int up = x % 10;
        if (low != up) return false;
        x = (x % div) / 10;
        div /= 100;
    }

    return true;
}


int main(int argc, char* argv[])
{

    ifstream fin(argv[1], ifstream::in);
    ofstream fout("output.txt", ofstream::out);

    int T = 0;
    fin >> T;

    for(int t=0; t < T; t++) {
        unsigned long long int lw;
        unsigned long long int up;
        unsigned long long int sqlw;
        unsigned long long int squp;
        unsigned long long int fsct = 0;
        

        fin >> lw;
        fin >> up;

        sqlw = (unsigned long long int)sqrt(lw);
				squp = (unsigned long long int)sqrt(up);

        /* search numbers till limit */
        for(unsigned long long int i = sqlw; i <= squp; i++) {
            unsigned long long int square = i*i;
            if(square >= lw && isPalindrome(i) && isPalindrome(square)) {
                fsct++;
            }
        }

        fout << "Case #" << t+1 << ": " << fsct << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
