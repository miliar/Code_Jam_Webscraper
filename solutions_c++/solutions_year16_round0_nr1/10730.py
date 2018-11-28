#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main() {

    int inputNumber=0;
    int T;



    ifstream infile;
    infile.open("A-large.in");
    string line;

    if(infile) {
        getline(infile, line);
        T = atoi(line.c_str());
        for (int k = 0; k < T; ++k) {
            getline(infile, line);
            inputNumber = atoi(line.c_str());
            bool found=false;

            bool seen[] = {0,0,0,0,0,0,0,0,0,0};
            int iCopy = inputNumber;
            int remainder;
            int lastNumber=inputNumber;

            for(int j=2 ; j<10000 ; j++) {

                while (inputNumber >= 1) {
                    remainder = inputNumber % 10;
                    inputNumber /= 10;
                    seen[remainder] = 1;
                }

                int i;
                for (i = 0; i < 10; i++) {
                    if (!seen[i]) {break; }
                }
                if (i == 10) {
                    cout << "Case #" << k+1 << ": " << lastNumber <<endl;
                    found=true;
                    break;
                }
                inputNumber = iCopy*j;
                lastNumber=inputNumber;
            }
            if(!found) {
                cout << "Case #" << k+1 << ": " <<"INSOMNIA" <<endl;
            }


        }
        infile.close();
    }
    else{
        cout<< "Couldn't open file" << endl;
    }









    return 0;
}