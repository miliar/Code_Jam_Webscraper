#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>

using namespace std;

unsigned long long int howMany(string pancakes){
    unsigned long long int n = 0;

    for (unsigned int i = 0; i < pancakes.length() - 1; i++) {
        if (pancakes[i] != pancakes[i+1])
            n++;
    }

    if (pancakes[pancakes.length() - 1] == '-')
        n++;

    return n;
}


int main()
{
    ifstream in ("B-large.in");
    ofstream out ("output.out");
    string pancakes;
    unsigned long long int T, result;
    //unsigned long long int time, n, timeUp, timeDown;

    if(in.is_open()){
        in >> T;
        for (unsigned int i = 1; i <= T; i++){
            in >> pancakes;
            result = howMany(pancakes);
            out << "Case #" << i << ": " << result << endl;
        }
        in.close();
    }
    out.close();
    return 0;
}
