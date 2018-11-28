#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>

using namespace std;


long long getDivisor(long long number) {
    if (number < 2) return -1;
    if (number == 2) return -1;
    if (number % 2 == 0) return 2;
    for (long long i=3; (i*i) <= number; i+=2) {
        if (number % i == 0 ) return i;
    }
    return -1;
}


int main() {
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");
    int T, digits ,neededJamcoins, okJamcoins;
    fin >> T;
    for(int t = 1; t <= T; t++){

        fin>>digits;
        fin>>neededJamcoins;
        fout << "Case #" << t << ":\n";

        okJamcoins = 0;

        for (int i=0; i<pow(2, digits-2); i++){
            string numString = bitset< 32 >( i ).to_string();
            numString = numString.substr(32-(digits-2), digits-2);
            char numStr[digits];
            numStr[0] = '1';
            strcpy(&numStr[1], numString.c_str());
            numStr[digits-1] = '1';
            bool isPrime = false;
            string outputLine = string(numStr);
            for (int j=2; j<=10; j++){
                char * end;
                long long numInterpretation = strtoll (numStr,&end,j);
                long long divisor = getDivisor(numInterpretation);
                if (divisor == -1){
                    isPrime = true;
                    break;
                }
                else{
                    outputLine += " " + to_string(divisor);
                }

            }

            if (!isPrime){
                fout << outputLine + "\n";
                okJamcoins++;
            }

            if (neededJamcoins == okJamcoins){
                break;
            }
        }

    }
    fin.close();
    fout.close();
    exit(0);
}

