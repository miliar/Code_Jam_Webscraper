#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

ofstream out;

void count(unsigned long long int K, unsigned long long int C, unsigned long long int S){
    for (int i = 1; i <= K; i++) {
        out << " " << i;
    }

    /*if (K % C == 0) {
        if (S < K/C) {
            out << "IMPOSIBLE";
            return;
        }

        for (int i = 1; i < K/C; i++) {

        }




    } else {
        if (S <= K/C) {
            out << "IMPOSIBLE";
        return;
        }


        for (int i = 1; i < K/C; i++) {

        }


        out << pow(K,C);
    }*/


}


int main()
{
    ifstream in ("D-small-attempt0.in");
    out.open("output.out");
    //string number;
    unsigned long long int T, K, C, S;
    //unsigned long long int time, n, timeUp, timeDown;

    if(in.is_open()){
        in >> T;
        for (unsigned int i = 1; i <= T; i++){
            in >> K >> C >> S;
            out << "Case #" << i << ":";
            count(K, C, S);
            out << endl;
        }
        in.close();
    }
    out.close();
    return 0;
}
