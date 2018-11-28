#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>

using namespace std;

ofstream out;

void result(unsigned long long int N, unsigned long long int J){
    unsigned int number[N/2];

    number[0] = 1;
    number[N/2-1] = 1;
    for (unsigned int j = 1; j < N/2 - 1; j++) {
        number[j] = 0;
    }
    for (unsigned int l = 0; l < 2; l++) {
        for (unsigned int k = 0; k < N/2; k++) {
        out << number[k];
        }
    }
    //out << " 257 6562 65537 390626 1679617 5764802 16777217 43046722 100000001" << endl;  //small
    out << " 65537 43046722 4294967297 152587890626 2821109907457 33232930569602 281474976710657 1853020188851842 10000000000000001" << endl; //big

    for (unsigned int i = 1; i < J; i++) {
        int j = 0;
        while (true) {
            if (number[N/2-2-j] == 1)
                number[N/2-2-j] = 0;
            else {
                number[N/2-2-j] = 1;
                break;
            }
            j++;
        }

        for (unsigned int l = 0; l < 2; l++) {
            for (unsigned int k = 0; k < N/2; k++) {
            out << number[k];
            }
        }
        //out << " 257 6562 65537 390626 1679617 5764802 16777217 43046722 100000001" << endl;  //small
        out << " 65537 43046722 4294967297 152587890626 2821109907457 33232930569602 281474976710657 1853020188851842 10000000000000001" << endl; //big
    }

    return;
}


int main()
{
    ifstream in ("C-large.in");
    out.open("output.out");
    //string pancakes;
    unsigned long long int T, J, N;
    //unsigned long long int time, n, timeUp, timeDown;

    if(in.is_open()){
        in >> T;
        for (unsigned int i = 1; i <= T; i++){
            in >> N >> J;
            out << "Case #" << i << ": " << endl;
            result(N, J);
        }
        in.close();
    }
    out.close();
    return 0;
}
