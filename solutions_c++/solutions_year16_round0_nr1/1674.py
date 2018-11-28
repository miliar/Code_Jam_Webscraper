#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>

using namespace std;

/*unsigned long long int lastNumber(string N){
    if (N == "0")
        return 0;
    int digits = 0;
    int i = 0;
    bool digit[10];
    for (int i = 0; i < 10; i++) {
        digit[i] = false;
    }

    while ((digits < 10) && (i < 100)) {
        for (unsigned int j = 0; j < N.length(); j++) {
            int n = N[j]-'0';
            if (digit[n] == false) {
                digit[n] = true;
                digits++;
            }
        }
        //treba zvacsit cislo
        i++;
    }
    return i;
}*/

unsigned long long int lastNumber(unsigned long long int number){
    unsigned long long int n = 0;
    string N = to_string(number);
    if (N == "0")
        return 0;

    int digits = 0;
    int i = 0;
    bool digit[10];
    for (int i = 0; i < 10; i++) {
        digit[i] = false;
    }

    do {
        n += number;
        N = to_string(n);
        i++;
        for (unsigned int j = 0; j < N.length(); j++) {
            int d = N[j]-'0';
            if (digit[d] == false) {
                digit[d] = true;
                digits++;
            }
        }
    } while (digits < 10);

    return n;
}


int main()
{
    ifstream in ("A-large.in");
    ofstream out ("output.out");
    //string number;
    unsigned long long int T, N, result;
    //unsigned long long int time, n, timeUp, timeDown;

    if(in.is_open()){
        in >> T;
        for (unsigned int i = 1; i <= T; i++){
            in >> N;
            result = lastNumber(N);
            if (result == 0) {
                out << "Case #" << i << ": " << "INSOMNIA" << endl;
            } else {
                out << "Case #" << i << ": " << result << endl;
            }
        }
        in.close();
    }
    out.close();
    return 0;
}
